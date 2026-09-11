"""Import the complete HeartGold & SoulSilver-era catalog and native art.

Printed data comes from the repository's pokemon-tcg-data snapshot.  Card
textures come from the original PTCGO archives in ``A:\\PTCGO`` (or the
directory passed with ``--source``).  Existing hand-written definitions are
never overwritten, so individual cards can be upgraded safely later.

Run from the repository root::

    python -m spirit.tools.import_hgss_sets --source A:\\PTCGO
"""

from __future__ import annotations

import argparse
import json
import re
import zipfile
from pathlib import Path, PurePosixPath
from typing import Any, Dict

from spirit.game.text_encoding import fix_mojibake as fix_text
from spirit.tools.import_standard_sets import (
    clean_name,
    download_one,
    existing_guid_scripts,
    existing_print_scripts,
    guid_for,
    mechanics_signature,
    module_for,
    numeric,
    render_energy,
    render_pokemon,
    render_reprint,
    render_trainer,
)
from spirit.tools.ptcgo_local_assets import (
    CARD_ARCHIVES,
    install_card_art,
    source_directory,
)


ROOT = Path(__file__).resolve().parents[2]
DATA_ROOT = (
    ROOT / "tools" / "card-builder" / "data" /
    "pokemon-tcg-data" / "cards" / "en"
)

# pokemon-tcg-data stem -> original PTCGO/server set key.
HGSS_SETS = {
    "hsp": "Promo_HGSS",
    "hgss1": "HGSS1",
    "hgss2": "HGSS2",
    "hgss3": "HGSS3",
    "hgss4": "HGSS4",
    "col1": "COL",
}

SPECIAL_NUMBERS = {
    ("hgss1", "ONE"): 124,
    ("hgss2", "TWO"): 96,
    ("hgss3", "THREE"): 91,
    ("hgss4", "FOUR"): 103,
}

ENERGY_TYPES = (
    "Grass", "Fire", "Water", "Lightning", "Psychic",
    "Fighting", "Darkness", "Metal",
)


def load_cards(stem: str) -> list[dict]:
    payload = json.loads((DATA_ROOT / f"{stem}.json").read_text(encoding="utf-8"))
    if not isinstance(payload, list):
        raise ValueError(f"Expected a card list in {stem}.json")
    return payload


def internal_number(card: dict, api_stem: str) -> int:
    """Map printed promo/secret labels to the client's numeric image slot."""
    printed = str(card.get("number") or "").strip().upper()
    special = SPECIAL_NUMBERS.get((api_stem, printed))
    if special is not None:
        return special
    shining = re.fullmatch(r"SL0*(\d+)", printed)
    if api_stem == "col1" and shining:
        return 95 + int(shining.group(1))
    return numeric(printed)


def collector_number_text(card: dict) -> str | None:
    """Preserve labels such as HGSS01, ONE and SL1 on the rendered card."""
    printed = fix_text(card.get("number", "")).strip()
    return printed if printed and not printed.isdigit() else None


def energy_profile(card: dict) -> dict:
    """Energy units and types used by the generic Energy definition."""
    name = fix_text(card.get("name", ""))
    special = "Special" in (card.get("subtypes") or [])
    profile: dict[str, Any] = {
        "energyKind": "special" if special else "basic",
        "provides": [],
    }
    if name == "Double Colorless Energy":
        profile["provides"] = ["any:Colorless,Colorless"]
    elif name == "Rainbow Energy":
        profile["providesAnyOf"] = list(ENERGY_TYPES)
    else:
        for energy_type in ENERGY_TYPES:
            if energy_type in name:
                profile["provides"] = [energy_type]
                break
        if not profile["provides"]:
            profile["provides"] = ["Colorless"]
    return profile


def _archive_for(source: Path, set_code: str) -> Path | None:
    suffix = CARD_ARCHIVES.get(set_code.upper())
    if not suffix:
        return None
    return next(
        (path for path in sorted(source.glob(f"*{suffix}"))
         if not path.name.endswith(" (1).zip")),
        None,
    )


def _archive_entries(archive: zipfile.ZipFile) -> dict[str, str]:
    entries: dict[str, str] = {}
    for name in archive.namelist():
        path = PurePosixPath(name)
        if path.suffix.lower() != ".png" or len(path.parts) != 2:
            continue
        if path.stem.isdigit():
            entries[str(int(path.stem))] = name
    return entries


def update_hgss_metadata() -> None:
    """Expose the six expansions in Legacy without changing official counts."""
    sets_path = ROOT / "spirit" / "database" / "json_data" / "sets.json"
    sets = json.loads(sets_path.read_text(encoding="utf-8"))
    for entry in sets:
        if entry.get("name") in HGSS_SETS.values():
            entry["filter"] = True
    sets_path.write_text(
        json.dumps(sets, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )

    formats_path = ROOT / "spirit" / "database" / "json_data" / "formats.json"
    payload = json.loads(formats_path.read_text(encoding="utf-8"))
    hgss = ["Promo_HGSS", "HGSS1", "HGSS2", "HGSS3", "HGSS4", "COL"]
    for fmt in payload.get("formats", []):
        if fmt.get("key") != "Legacy":
            continue
        remaining = [code for code in fmt.get("sets", []) if code not in hgss]
        insert_at = 1 if remaining and remaining[0] == "Free_Energy" else 0
        fmt["sets"] = remaining[:insert_at] + hgss + remaining[insert_at:]
    formats_path.write_text(
        json.dumps(payload, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )


def run(selected: set[str], source: Path, download_missing: bool = False) -> None:
    guid_scripts = existing_guid_scripts()
    print_scripts = existing_print_scripts()
    generated_signatures: Dict[str, str] = {}
    all_cards = {stem: load_cards(stem) for stem in HGSS_SETS}
    created = reprints = skipped = art_written = art_missing = 0

    for api_stem, set_code in HGSS_SETS.items():
        if selected and api_stem not in selected and set_code.lower() not in selected:
            continue
        cards = all_cards[api_stem]
        by_name = {
            fix_text(card.get("name", "")): card
            for card in cards
            if fix_text(card.get("supertype", "")).startswith("Pok")
        }
        scripts_dir = ROOT / "spirit" / "game" / "scripts" / "cards" / set_code
        assets_dir = ROOT / "spirit" / "assets" / "cards" / set_code
        scripts_dir.mkdir(parents=True, exist_ok=True)
        assets_dir.mkdir(parents=True, exist_ok=True)

        archive_path = _archive_for(source, set_code)
        archive = zipfile.ZipFile(archive_path) if archive_path else None
        archive_entries = _archive_entries(archive) if archive else {}
        try:
            for original in cards:
                card = dict(original)
                number = internal_number(card, api_stem)
                printed = collector_number_text(original)
                card["number"] = str(number)
                if printed:
                    card["_collector_number_text"] = printed
                name = fix_text(card.get("name", "Unknown"))
                card["name"] = name
                stem = f"{clean_name(name)}_{number}"
                script_path = scripts_dir / f"{stem}.py"
                card_guid = guid_for(str(original.get("id") or f"{set_code}-{number}"))
                registered = (
                    guid_scripts.get(card_guid.lower())
                    or print_scripts.get((set_code, number))
                )
                asset_stem = (
                    registered.stem
                    if registered is not None and registered.parent == scripts_dir
                    else stem
                )
                asset_path = assets_dir / f"{asset_stem}.png"
                supertype = fix_text(card.get("supertype", ""))
                kind = "pokemon" if supertype.startswith("Pok") else supertype.lower()

                if registered is not None or script_path.exists():
                    skipped += 1
                else:
                    signature = mechanics_signature(original)
                    # A thin reprint clone cannot override the client's
                    # printed collector label, so special-number cards keep a
                    # complete definition even when their mechanics match.
                    base_module = None if printed else generated_signatures.get(signature)
                    if base_module:
                        source_text = render_reprint(card, set_code, base_module)
                        reprints += 1
                    elif kind == "pokemon":
                        source_text = render_pokemon(card, set_code, by_name)
                    elif kind == "trainer":
                        source_text = render_trainer(card, set_code)
                    elif kind == "energy":
                        source_text = render_energy(card, energy_profile(original), set_code)
                    else:
                        raise ValueError(
                            f"Unknown supertype {supertype!r} for {set_code}/{number}"
                        )
                    script_path.write_text(source_text, encoding="utf-8")
                    guid_scripts[card_guid.lower()] = script_path
                    print_scripts[(set_code, number)] = script_path
                    generated_signatures.setdefault(signature, module_for(script_path))
                    created += 1

                entry = archive_entries.get(str(number))
                if archive is not None and entry is not None:
                    payload = archive.read(entry)
                    if not asset_path.exists() or asset_path.read_bytes() != payload:
                        asset_path.write_bytes(payload)
                        art_written += 1
                elif install_card_art(
                    set_code, number, asset_path, source, overwrite=True
                ):
                    art_written += 1
                else:
                    url = (original.get("images") or {}).get("large")
                    if download_missing and url:
                        ok, detail = download_one((url, asset_path))
                        if ok:
                            art_written += 1
                        else:
                            print(f"[art] {detail}")
                            art_missing += 1
                    else:
                        art_missing += 1
        finally:
            if archive is not None:
                archive.close()

        print(
            f"{api_stem:6} -> {set_code:12}: {len(cards):3} cards, "
            f"{len(list(scripts_dir.glob('*.py'))):3} scripts"
        )

    # HGSS3's Alph Lithograph is internal slot 91, while the original foil
    # cache retained the native texture name 124.
    alias_dir = ROOT / "spirit" / "assets" / "cards" / "HGSS3"
    alias_dir.mkdir(parents=True, exist_ok=True)
    (alias_dir / "foil_aliases.json").write_text(
        json.dumps({"91": "124"}, indent=2) + "\n", encoding="utf-8"
    )
    update_hgss_metadata()
    print(
        f"Scripts created: {created} ({reprints} linked exact reprints); "
        f"existing: {skipped}; art updated: {art_written}; "
        f"missing art: {art_missing}"
    )


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("sets", nargs="*", help="Optional API stem or set code")
    parser.add_argument("--source", help="PTCGO source directory")
    parser.add_argument(
        "--download-missing", action="store_true",
        help="Download only textures absent from the original local archives",
    )
    args = parser.parse_args()
    run(
        {value.lower() for value in args.sets},
        source_directory(args.source).resolve(),
        args.download_missing,
    )


if __name__ == "__main__":
    main()
