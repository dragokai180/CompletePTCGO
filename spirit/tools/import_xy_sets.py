"""Import the complete XY-era catalog without replacing bespoke scripts.

Card definitions come from the repository's local pokemon-tcg-data snapshot;
original card textures come from the configured PTCGO directory.  Existing
hand-written cards always win.  Exact Trainer/Energy reprints link to their
already implemented definition, while other cards use the shared printed-text
engine.

Run from the repository root::

    python -m spirit.tools.import_xy_sets --source A:\\PTCGO
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
    existing_named_modules,
    existing_print_scripts,
    guid_for,
    mechanics_signature,
    module_for,
    numeric,
    render_energy,
    render_pokemon,
    render_reprint,
    render_trainer,
    update_metadata,
)
from spirit.tools.ptcgo_local_assets import (
    CARD_ARCHIVES,
    install_card_art,
    source_directory,
)


ROOT = Path(__file__).resolve().parents[2]
DATA_ROOT = ROOT / "tools" / "card-builder" / "data" / "pokemon-tcg-data" / "cards" / "en"

# pokemon-tcg-data stem -> server/PTCGO set code.
XY_SETS = {
    "xy0": "XY0",
    "xy1": "XY1",
    "xy2": "XY2",
    "xy3": "XY3",
    "xy4": "XY4",
    "xy5": "XY5",
    "dc1": "TATM",
    "xy6": "XY6",
    "xy7": "XY7",
    "xy8": "XY8",
    "xy9": "XY9",
    "g1": "TwentiethAnn",
    "xy10": "XY10",
    "xy11": "XY11",
    "xy12": "XY12",
    "xyp": "Promo_XY",
}

# Promo alternates have the same printed number in pokemon-tcg-data.  Internal
# unique collector slots keep both physical prints addressable by AutoBundle.
PROMO_ALT_NUMBERS = {
    "XY67a": 212,
    "XY150a": 213,
    "XY177a": 214,
    "XY198a": 215,
    "XY200a": 216,
}

ALT_INTERNAL_NUMBERS = {
    "xy2-88a": 111,
    "xy3-55a": 114,
    "xy4-24a": 125,
    "xy4-65a": 126,
    "xy6-77a": 113,
    "xy6-92a": 114,
    "xy7-75a": 102,
    "xy8-146a": 166,
    "xy9-98a": 127,
    "xy9-98b": 128,
    "xy9-107a": 129,
    "g1-28a": 133,
    "g1-73a": 134,
    "xy10-43a": 130,
    "xy10-54a": 131,
    "xy10-105a": 132,
    "xy10-111a": 133,
}

ENERGY_TYPES = (
    "Grass", "Fire", "Water", "Lightning", "Psychic",
    "Fighting", "Darkness", "Metal", "Fairy",
)


def load_cards(stem: str) -> list[dict]:
    payload = json.loads((DATA_ROOT / f"{stem}.json").read_text(encoding="utf-8"))
    if not isinstance(payload, list):
        raise ValueError(f"Expected a card list in {stem}.json")
    return payload


def internal_number(card: dict, api_stem: str) -> int:
    number = str(card.get("number") or "")
    card_id = str(card.get("id") or "")
    if card_id in ALT_INTERNAL_NUMBERS:
        return ALT_INTERNAL_NUMBERS[card_id]
    if api_stem == "g1" and number.upper().startswith("RC"):
        return 100 + numeric(number)
    if api_stem == "xyp":
        promo_id = re.sub(r"^xyp-", "", str(card.get("id") or ""), flags=re.I)
        return PROMO_ALT_NUMBERS.get(promo_id, numeric(number))
    return numeric(number)


def energy_profile(card: dict) -> dict:
    """Minimal provider metadata consumed by the generic Energy renderer."""
    name = fix_text(card.get("name", ""))
    special = "Special" in (card.get("subtypes") or [])
    result: dict[str, Any] = {
        "energyKind": "special" if special else "basic",
        "provides": [],
    }
    if name == "Double Colorless Energy":
        result["provides"] = ["any:Colorless,Colorless"]
    elif name == "Double Aqua Energy":
        result["provides"] = ["any:Water,Water"]
    elif name == "Double Magma Energy":
        result["provides"] = ["any:Fighting,Fighting"]
    elif name in ("Rainbow Energy", "Double Dragon Energy"):
        result["providesAnyOf"] = list(ENERGY_TYPES)
    else:
        for energy_type in ENERGY_TYPES:
            if energy_type in name:
                result["provides"] = [energy_type]
                break
        if not result["provides"]:
            # Type-gated XY Special Energy uses the target's printed type.
            rules = " ".join(card.get("rules") or [])
            match = re.search(
                r"provides (Grass|Fire|Water|Lightning|Psychic|Fighting|"
                r"Darkness|Metal|Fairy) Energy",
                rules,
                re.I,
            )
            result["provides"] = [match.group(1).title() if match else "Colorless"]
    return result


def _archive_for(source: Path, set_code: str) -> Path | None:
    suffix = CARD_ARCHIVES.get(set_code.upper())
    if not suffix:
        return None
    return next((path for path in sorted(source.glob(f"*{suffix}"))
                 if not path.name.endswith(" (1).zip")), None)


def _archive_entries(archive: zipfile.ZipFile) -> dict[str, str]:
    entries: dict[str, str] = {}
    for name in archive.namelist():
        path = PurePosixPath(name)
        if path.suffix.lower() != ".png" or len(path.parts) != 2:
            continue
        key = path.stem.lower().lstrip("0") or "0"
        if key.isdigit() or re.fullmatch(r"\d+xy", key):
            entries[key] = name
        gold = re.fullmatch(r"0*(\d+)_gold", path.stem, re.I)
        if gold:
            entries.setdefault(str(int(gold.group(1))), name)
    return entries


def _art_key(card: dict, api_stem: str, number: int) -> str:
    card_id = str(card.get("id", "")).lower()
    if card_id in ALT_INTERNAL_NUMBERS or (
        api_stem == "xyp" and card_id.endswith("a")
    ):
        printed = numeric(card.get("number"))
        return f"{printed}xy"
    return str(number)


def run(selected: set[str], source: Path, download_missing: bool = False) -> None:
    named_modules = existing_named_modules()
    guid_scripts = existing_guid_scripts()
    print_scripts = existing_print_scripts()
    generated_signatures: Dict[str, str] = {}
    all_cards = {stem: load_cards(stem) for stem in XY_SETS}
    created = reprints = skipped = art_written = art_missing = 0
    counts: Dict[str, int] = {}

    # Existing bespoke XY Pokemon seed exact-print reprints without ever
    # linking merely by name (different Pokemon cards often share a name).
    for api_stem, set_code in XY_SETS.items():
        for original in all_cards[api_stem]:
            number = internal_number(original, api_stem)
            path = print_scripts.get((set_code, number))
            if path is not None and fix_text(original.get("supertype", "")).startswith("Pok"):
                generated_signatures.setdefault(
                    mechanics_signature(original), module_for(path)
                )

    for api_stem, set_code in XY_SETS.items():
        if selected and api_stem not in selected and set_code.lower() not in selected:
            continue
        cards = all_cards[api_stem]
        by_name = {
            fix_text(card.get("name", "")): card for card in cards
            if fix_text(card.get("supertype", "")).startswith("Pok")
        }
        counts[set_code] = max((internal_number(card, api_stem) for card in cards), default=0)
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
                card["number"] = str(number)
                name = fix_text(card.get("name", "Unknown"))
                card["name"] = name
                stem = f"{clean_name(name)}_{number}"
                script_path = scripts_dir / f"{stem}.py"
                card_guid = guid_for(str(original.get("id") or f"{set_code}-{number}"))
                registered = (
                    guid_scripts.get(card_guid.lower())
                    or print_scripts.get((set_code, number))
                )
                asset_stem = registered.stem if registered is not None \
                    and registered.parent == scripts_dir else stem
                asset_path = assets_dir / f"{asset_stem}.png"
                supertype = fix_text(card.get("supertype", ""))
                kind = "pokemon" if supertype.startswith("Pok") else supertype.lower()

                if registered is not None or script_path.exists():
                    skipped += 1
                else:
                    base_module = None
                    if kind == "pokemon":
                        base_module = generated_signatures.get(mechanics_signature(original))
                    elif kind in ("trainer", "energy"):
                        base_module = named_modules.get((kind, name))
                    if base_module:
                        source_text = render_reprint(card, set_code, base_module)
                        reprints += 1
                    elif kind == "pokemon":
                        source_text = render_pokemon(card, set_code, by_name)
                    elif kind == "trainer":
                        source_text = render_trainer(card, set_code)
                    elif kind == "energy":
                        source_text = render_energy(
                            card, energy_profile(original), set_code
                        )
                    else:
                        raise ValueError(
                            f"Unknown supertype {supertype!r} for {set_code}/{number}"
                        )
                    script_path.write_text(source_text, encoding="utf-8")
                    guid_scripts[card_guid.lower()] = script_path
                    print_scripts[(set_code, number)] = script_path
                    created += 1
                    if kind == "pokemon":
                        generated_signatures.setdefault(
                            mechanics_signature(original), module_for(script_path)
                        )
                    else:
                        named_modules.setdefault((kind, name), module_for(script_path))

                key = _art_key(original, api_stem, number).lower().lstrip("0") or "0"
                entry = archive_entries.get(key)
                # XY67a is not present as a separate local texture; retain the
                # corresponding normal promo instead of falling back to web art.
                if entry is None and api_stem == "xyp" and key.endswith("xy"):
                    entry = archive_entries.get(key[:-2])
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
                        if not ok and api_stem == "xyp":
                            fallback_url = (
                                "https://images.pokemontcg.io/xyp/"
                                f"{numeric(original.get('number'))}_hires.png"
                            )
                            ok, detail = download_one((fallback_url, asset_path))
                        if not ok and api_stem == "xyp":
                            fallback_url = (
                                "https://limitlesstcg.nyc3.cdn.digitaloceanspaces.com/"
                                "tpci/PR-XY/PR-XY_"
                                f"{numeric(original.get('number')):03d}_R_EN.png"
                            )
                            ok, detail = download_one((fallback_url, asset_path))
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
            f"{api_stem:5} -> {set_code:14}: {len(cards):3} cards, "
            f"{len(list(scripts_dir.glob('*.py'))):3} scripts"
        )

    update_metadata(counts)
    print(
        f"Scripts created: {created} ({reprints} linked reprints); "
        f"existing: {skipped}; art updated: {art_written}; missing art: {art_missing}"
    )


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("sets", nargs="*", help="Optional API stem or server set code")
    parser.add_argument("--source", help="PTCGO source directory")
    parser.add_argument(
        "--download-missing", action="store_true",
        help="Use pokemon-tcg-data only for textures absent from the local cache",
    )
    args = parser.parse_args()
    run(
        {value.lower() for value in args.sets},
        source_directory(args.source).resolve(),
        args.download_missing,
    )


if __name__ == "__main__":
    main()
