"""Import the complete Scarlet & Violet era without replacing bespoke cards.

Printed definitions and English artwork URLs come from the repository's
pokemon-tcg-data snapshot.  Existing hand-written cards always win.  Exact
Pokemon reprints and named Trainer/Energy reprints reuse their authoritative
implementation, while new prints use the shared modern-text engine.

Run from the repository root::

    python -m spirit.tools.import_sv_sets --download-missing
"""

from __future__ import annotations

import argparse
import json
import re
from collections import OrderedDict
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
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
)


ROOT = Path(__file__).resolve().parents[2]
DATA_ROOT = (
    ROOT / "tools" / "card-builder" / "data" /
    "pokemon-tcg-data" / "cards" / "en"
)

# pokemon-tcg-data stem -> (server set code, external id, display order).
# The decimal mini-sets use a zero-padded server code, matching the convention
# already established by SV05/SV065/SV085 in this repository.
SV_SETS = OrderedDict([
    ("sve", ("SVE", "SVE", 1110)),
    ("sv1", ("SV1", "SVI", 1120)),
    ("sv2", ("SV2", "PAL", 1130)),
    ("sv3", ("SV3", "OBF", 1140)),
    ("sv3pt5", ("SV035", "MEW", 1145)),
    ("sv4", ("SV4", "PAR", 1150)),
    ("sv4pt5", ("SV045", "PAF", 1155)),
    ("sv5", ("SV05", "TEF", 1160)),
    ("sv6", ("SV06", "TWM", 1170)),
    ("sv6pt5", ("SV065", "SFA", 1175)),
    ("sv7", ("SV07", "SCR", 1180)),
    ("sv8", ("SV08", "SSP", 1190)),
    ("sv8pt5", ("SV085", "PRE", 1195)),
    ("sv9", ("SV09", "JTG", 1200)),
    ("sv10", ("SV10", "DRI", 1210)),
    ("rsv10pt5", ("RSV10PT5", "WHT", 1220)),
    ("zsv10pt5", ("ZSV10PT5", "BLK", 1230)),
    ("svp", ("SVP", "PR-SV", 1240)),
])

SET_NAMES = {
    "SVE": "Scarlet & Violet Energies",
    "SV1": "Scarlet & Violet",
    "SV2": "Scarlet & Violet—Paldea Evolved",
    "SV3": "Scarlet & Violet—Obsidian Flames",
    "SV035": "Scarlet & Violet—151",
    "SV4": "Scarlet & Violet—Paradox Rift",
    "SV045": "Scarlet & Violet—Paldean Fates",
    "SV05": "Scarlet & Violet—Temporal Forces",
    "SV06": "Scarlet & Violet—Twilight Masquerade",
    "SV065": "Scarlet & Violet—Shrouded Fable",
    "SV07": "Scarlet & Violet—Stellar Crown",
    "SV08": "Scarlet & Violet—Surging Sparks",
    "SV085": "Scarlet & Violet—Prismatic Evolutions",
    "SV09": "Scarlet & Violet—Journey Together",
    "SV10": "Scarlet & Violet—Destined Rivals",
    "RSV10PT5": "Scarlet & Violet—White Flare",
    "ZSV10PT5": "Scarlet & Violet—Black Bolt",
    "SVP": "Scarlet & Violet Black Star Promos",
}

ENERGY_TYPES = (
    "Grass", "Fire", "Water", "Lightning", "Psychic",
    "Fighting", "Darkness", "Metal", "Fairy",
)

FORMAT_GUIDS = [
    "6402e830-7fed-4cd1-b172-2a320047c2bb",  # Standard
    "98c83df9-ec82-4193-84a8-104115ce4e25",  # Expanded
    "6a1dec5a-34db-4cee-a503-4ee759304135",  # Unlimited
]

# pokemon-tcg-data currently points this print at a non-existent
# images.pokemontcg.io object.  Keep the verified English scan explicit so a
# future idempotent import does not regress to a missing texture.
IMAGE_OVERRIDES = {
    "svp-102": "https://pkmncards.com/wp-content/uploads/svbsp_en_102_std.png",
}


def load_cards(stem: str) -> list[dict]:
    path = DATA_ROOT / f"{stem}.json"
    payload = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(payload, list):
        raise ValueError(f"Expected a card list in {path}")
    return payload


def energy_profile(card: dict) -> dict:
    """Provider metadata consumed by the generic Energy renderer."""
    name = fix_text(card.get("name", ""))
    text = " ".join(fix_text(rule) for rule in card.get("rules") or [])
    special = "Special" in (card.get("subtypes") or [])
    result: dict[str, Any] = {
        "energyKind": "special" if special else "basic",
        "provides": [],
    }

    # Luminous and Reversal can become every type.  Their conditional state is
    # interpreted by the attached passive; listing all types here gives the
    # payment selector the complete set of legal type choices.
    if "provides every type of Energy" in text:
        result["providesAnyOf"] = list(ENERGY_TYPES)
    else:
        match = re.search(
            r"provides (Grass|Fire|Water|Lightning|Psychic|Fighting|"
            r"Darkness|Metal|Fairy|Colorless) Energy",
            text,
            re.IGNORECASE,
        )
        if match:
            result["provides"] = [match.group(1).title()]
        else:
            for energy_type in ENERGY_TYPES:
                if energy_type in name:
                    result["provides"] = [energy_type]
                    break
    if not result.get("provides") and not result.get("providesAnyOf"):
        result["provides"] = ["Colorless"]
    return result


def _set_metadata(counts: Dict[str, int]) -> None:
    sets_path = ROOT / "spirit" / "database" / "json_data" / "sets.json"
    sets = json.loads(sets_path.read_text(encoding="utf-8"))
    by_name = {entry["name"]: entry for entry in sets}
    for _stem, (code, external_id, order) in SV_SETS.items():
        if code not in counts:
            continue
        record = by_name.get(code)
        values = {
            "count": counts[code],
            "filter": True,
            "visibleUnfilterable": False,
        }
        if record is None:
            legal_formats = list(FORMAT_GUIDS) if code == "SVE" else FORMAT_GUIDS[1:]
            record = {
                "name": code,
                "externalId": external_id,
                "number": order,
                "block": "SV",
                "legalFormats": legal_formats,
                "featuredArchetypes": [],
                "promo": code == "SVP",
            }
            sets.append(record)
            by_name[code] = record
        record.update(values)
    sets_path.write_text(
        json.dumps(sets, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )

    formats_path = ROOT / "spirit" / "database" / "json_data" / "formats.json"
    formats = json.loads(formats_path.read_text(encoding="utf-8"))
    imported = list(counts)
    for fmt in formats.get("formats", []):
        key = fmt.get("key")
        if key in ("Expanded", "Unlimited"):
            for code in imported:
                if code not in fmt["sets"]:
                    fmt["sets"].append(code)
        elif key in ("Standard", "StandardNightly") and "SVE" in imported:
            if "SVE" not in fmt["sets"]:
                fmt["sets"].append("SVE")
    formats_path.write_text(
        json.dumps(formats, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )


def _update_localization() -> None:
    path = ROOT / "spirit" / "game" / "localization_overrides.py"
    source = path.read_text(encoding="utf-8")
    marker = '    # Scarlet & Violet expansions present in this server.\n'
    if marker not in source:
        raise ValueError("Scarlet & Violet localization marker is missing")
    additions = "".join(
        f'    "set.name.{code.lower()}": "<i>{name}</i>",\n'
        for code, name in SET_NAMES.items()
        if f'"set.name.{code.lower()}"' not in source
    )
    if additions:
        source = source.replace(marker, marker + additions)
        path.write_text(source, encoding="utf-8")


def run(selected: set[str], download_missing: bool, workers: int) -> None:
    named_modules = existing_named_modules()
    guid_scripts = existing_guid_scripts()
    print_scripts = existing_print_scripts()
    generated_signatures: Dict[str, str] = {}
    all_cards = {stem: load_cards(stem) for stem in SV_SETS}
    created = reprints = skipped = 0
    image_tasks: list[tuple[str, Path]] = []
    counts: Dict[str, int] = {}

    # Seed exact Pokemon signatures from every already implemented SV print,
    # including bespoke cards in later expansions.
    for api_stem, (set_code, _external_id, _order) in SV_SETS.items():
        for original in all_cards[api_stem]:
            number = numeric(original.get("number"))
            path = print_scripts.get((set_code, number))
            if path is not None and fix_text(
                original.get("supertype", "")
            ).startswith("Pok"):
                generated_signatures.setdefault(
                    mechanics_signature(original), module_for(path)
                )

    for api_stem, (set_code, _external_id, _order) in SV_SETS.items():
        if selected and api_stem not in selected and set_code.lower() not in selected:
            continue
        cards = all_cards[api_stem]
        by_name = {
            fix_text(card.get("name", "")): card for card in cards
            if fix_text(card.get("supertype", "")).startswith("Pok")
        }
        scripts_dir = ROOT / "spirit" / "game" / "scripts" / "cards" / set_code
        assets_dir = ROOT / "spirit" / "assets" / "cards" / set_code
        scripts_dir.mkdir(parents=True, exist_ok=True)
        assets_dir.mkdir(parents=True, exist_ok=True)

        for original in cards:
            card = dict(original)
            number = numeric(card.get("number"))
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
                    base_module = generated_signatures.get(
                        mechanics_signature(original)
                    )
                elif kind in ("trainer", "energy"):
                    base_module = named_modules.get((kind, name))

                if base_module:
                    source = render_reprint(card, set_code, base_module)
                    reprints += 1
                elif kind == "pokemon":
                    source = render_pokemon(card, set_code, by_name)
                elif kind == "trainer":
                    source = render_trainer(card, set_code)
                elif kind == "energy":
                    source = render_energy(
                        card, energy_profile(original), set_code
                    )
                else:
                    raise ValueError(
                        f"Unknown supertype {supertype!r} for {set_code}/{number}"
                    )
                script_path.write_text(source, encoding="utf-8")
                guid_scripts[card_guid.lower()] = script_path
                print_scripts[(set_code, number)] = script_path
                created += 1
                if kind == "pokemon":
                    generated_signatures.setdefault(
                        mechanics_signature(original), module_for(script_path)
                    )
                else:
                    named_modules.setdefault((kind, name), module_for(script_path))

            if not asset_path.exists():
                url = IMAGE_OVERRIDES.get(str(original.get("id") or "")) or (
                    original.get("images") or {}
                ).get("large")
                if url:
                    image_tasks.append((url, asset_path))

        # Promo catalogs can contain later, already implemented prints that
        # are newer than the pokemon-tcg-data snapshot.  Preserve those files
        # and report the actual number of available physical prints.
        counts[set_code] = len(list(scripts_dir.glob("*.py")))

        print(
            f"{api_stem:9} -> {set_code:10}: {len(cards):3} cards, "
            f"{len(list(scripts_dir.glob('*.py'))):3} scripts"
        )

    _set_metadata(counts)
    _update_localization()
    print(
        f"Scripts created: {created} ({reprints} linked reprints); "
        f"existing: {skipped}"
    )

    if not download_missing:
        print(f"Images still missing: {len(image_tasks)} (rerun with --download-missing)")
        return
    failures = []
    done = 0
    with ThreadPoolExecutor(max_workers=workers) as pool:
        futures = [pool.submit(download_one, task) for task in image_tasks]
        for future in as_completed(futures):
            ok, detail = future.result()
            done += 1
            if not ok:
                failures.append(detail)
            if done % 100 == 0 or done == len(futures):
                print(f"Images: {done}/{len(futures)} ({len(failures)} failures)")
    if failures:
        print("Image download failures:")
        for failure in failures:
            print("  " + failure)
        raise SystemExit(2)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("sets", nargs="*", help="Optional API stem or server set code")
    parser.add_argument("--download-missing", action="store_true")
    parser.add_argument("--workers", type=int, default=20)
    args = parser.parse_args()
    run(
        {value.lower() for value in args.sets},
        args.download_missing,
        args.workers,
    )


if __name__ == "__main__":
    main()
