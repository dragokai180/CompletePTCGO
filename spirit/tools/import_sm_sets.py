"""Import the complete Sun & Moon era without replacing bespoke cards.

Printed definitions come from the repository's pokemon-tcg-data snapshot.
Original artwork and foil masks are resolved against the local PTCGO cache;
web art is only an explicit fallback for textures absent from that cache.

Run from the repository root::

    python -m spirit.tools.import_sm_sets --source A:\\PTCGO --download-missing
"""

from __future__ import annotations

import argparse
import io
import json
import re
import zipfile
from collections import OrderedDict
from pathlib import Path, PurePosixPath
from typing import Any, Dict

import UnityPy

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
from spirit.tools.ptcgo_local_assets import CARD_ARCHIVES, source_directory


ROOT = Path(__file__).resolve().parents[2]
DATA_ROOT = (
    ROOT / "tools" / "card-builder" / "data" /
    "pokemon-tcg-data" / "cards" / "en"
)

# pokemon-tcg-data stem -> original PTCGO/server set code.  Shiny Vault was
# part of Hidden Fates in PTCGO, so its 94 cards use reserved numeric slots in
# the same HF set instead of colliding with Hidden Fates 1-69.
SM_SETS = OrderedDict([
    ("sm1", "SM1"),
    ("smp", "Promo_SM"),
    ("sm2", "SM2"),
    ("sm3", "SM3"),
    ("sm35", "SL"),
    ("sm4", "SM4"),
    ("sm5", "SM5"),
    ("sm6", "SM6"),
    ("sm7", "SM7"),
    ("sm75", "DM"),
    ("sm8", "SM8"),
    ("sm9", "SM9"),
    ("det1", "GUM"),
    ("sm10", "SM10"),
    ("sm11", "SM11"),
    ("sm115", "HF"),
    ("sma", "HF"),
    ("sm12", "SM12"),
])

ENERGY_TYPES = (
    "Grass", "Fire", "Water", "Lightning", "Psychic",
    "Fighting", "Darkness", "Metal", "Fairy",
)


def load_cards(stem: str) -> list[dict]:
    payload = json.loads((DATA_ROOT / f"{stem}.json").read_text(encoding="utf-8"))
    if not isinstance(payload, list):
        raise ValueError(f"Expected a card list in {stem}.json")
    return payload


def number_map(cards: list[dict], api_stem: str) -> dict[str, int]:
    """Allocate stable numeric protocol slots for every physical print."""
    if api_stem == "sma":
        return {str(card["id"]): 100 + numeric(card.get("number")) for card in cards}
    ordinary = [numeric(card.get("number")) for card in cards
                if str(card.get("number") or "").isdigit()
                or api_stem == "smp" and re.fullmatch(r"SM\d+", str(card.get("number")), re.I)]
    next_slot = max(ordinary, default=0) + 1
    result: dict[str, int] = {}
    for card in cards:
        value = str(card.get("number") or "")
        if value.isdigit() or api_stem == "smp" and re.fullmatch(r"SM\d+", value, re.I):
            result[str(card["id"])] = numeric(value)
        else:
            result[str(card["id"])] = next_slot
            next_slot += 1
    return result


def energy_profile(card: dict) -> dict:
    name = fix_text(card.get("name", ""))
    rules = " ".join(fix_text(rule) for rule in card.get("rules") or [])
    special = "Special" in (card.get("subtypes") or [])
    result: dict[str, Any] = {
        "energyKind": "special" if special else "basic",
        "provides": [],
    }
    if name in ("Double Colorless Energy", "Double Colorless Energy {*} "):
        result["provides"] = ["any:Colorless,Colorless"]
    elif name in ("Rainbow Energy", "Unit Energy {G}{R}{W}",
                  "Unit Energy {L}{P}{M}", "Unit Energy {F}{D}{Y}"):
        result["providesAnyOf"] = list(ENERGY_TYPES)
    else:
        match = re.search(
            r"provides (Grass|Fire|Water|Lightning|Psychic|Fighting|"
            r"Darkness|Metal|Fairy|Colorless) Energy", rules, re.I,
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


def _archive_for(source: Path, set_code: str) -> Path | None:
    suffix = CARD_ARCHIVES.get(set_code.upper())
    if not suffix:
        return None
    return next((path for path in sorted(source.glob(f"*{suffix}"))
                 if not path.name.endswith(" (1).zip")), None)


def _archive_entries(archive: zipfile.ZipFile) -> dict[str, bytes]:
    entries: dict[str, bytes] = {}
    for name in archive.namelist():
        path = PurePosixPath(name)
        if path.suffix.lower() != ".png" or len(path.parts) != 2:
            continue
        match = re.fullmatch(r"0*(\d+)(xy|ya|yb|a|b)?", path.stem, re.I)
        if match:
            key = str(int(match.group(1))) + (match.group(2) or "").lower()
            entries[key] = archive.read(name)
            continue
        gold = re.fullmatch(r"0*(\d+)_gold", path.stem, re.I)
        if gold:
            entries.setdefault(str(int(gold.group(1))), archive.read(name))
    return entries


def _cache_entries(source: Path, set_code: str) -> dict[str, bytes]:
    entries: dict[str, bytes] = {}
    cache = source / "SM Cache.zip"
    if not cache.is_file():
        return entries
    with zipfile.ZipFile(cache) as archive:
        prefix = f"en_US_{set_code}_".casefold()
        # The cache keeps several historical revisions of each type bundle.
        # Decode only the newest revision; older versions make a complete-era
        # import many times slower and cannot contain a newer card texture.
        newest: dict[str, zipfile.ZipInfo] = {}
        for info in archive.infolist():
            normalized = info.filename.replace("\\", "/")
            if not normalized.endswith("/__data") or "/bundleCache/" not in normalized:
                continue
            bundle = normalized.split("/bundleCache/", 1)[1].split("/", 1)[0]
            lowered = bundle.casefold()
            if not lowered.startswith(prefix) or "_wp_" in lowered:
                continue
            family = re.sub(r"_CR[^/]+$", "", bundle, flags=re.I)
            previous = newest.get(family)
            if previous is None or info.header_offset > previous.header_offset:
                newest[family] = info
        for info in newest.values():
            try:
                environment = UnityPy.load(archive.read(info))
                for obj in environment.objects:
                    if obj.type.name != "Texture2D":
                        continue
                    texture = obj.read()
                    if int(texture.m_Width) < 512 or int(texture.m_Height) < 512:
                        continue
                    key = str(texture.m_Name).strip().lower().lstrip("0") or "0"
                    if not re.fullmatch(r"\d+(?:xy|ya|yb|a|b)?", key):
                        continue
                    output = io.BytesIO()
                    texture.image.convert("RGBA").save(output, format="PNG")
                    entries[key] = output.getvalue()
            except Exception as exc:
                print(f"[art] could not inspect {info.filename}: {exc}")
    return entries


def _variant_key(card: dict, available: dict[str, bytes]) -> str | None:
    printed = str(numeric(card.get("number")))
    raw = str(card.get("number") or "").lower()
    if raw.isdigit() or re.fullmatch(r"sm\d+", raw):
        return printed if printed in available else None
    suffix = raw[-1:] if raw[-1:].isalpha() else "a"
    preferences = (
        ("xy", "ya", "a") if suffix == "a" else
        ("yb", "b", "ya", "xy")
    )
    for ending in preferences:
        key = printed + ending
        if key in available:
            return key
    return printed if printed in available else None


def _metadata(counts: Dict[str, int]) -> None:
    update_metadata(counts)
    path = ROOT / "spirit" / "database" / "json_data" / "formats.json"
    payload = json.loads(path.read_text(encoding="utf-8"))
    codes = list(dict.fromkeys(SM_SETS.values()))
    for fmt in payload.get("formats", []):
        if fmt.get("key") != "Expanded":
            continue
        for code in codes:
            if code not in fmt["sets"]:
                fmt["sets"].append(code)
    path.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n",
                    encoding="utf-8")


def run(selected: set[str], source: Path, download_missing: bool = False) -> None:
    named_modules = existing_named_modules()
    guid_scripts = existing_guid_scripts()
    print_scripts = existing_print_scripts()
    signatures: Dict[str, str] = {}
    loaded = {stem: load_cards(stem) for stem in SM_SETS}
    maps = {stem: number_map(cards, stem) for stem, cards in loaded.items()}
    created = reprints = skipped = art_written = art_missing = 0
    counts: Dict[str, int] = {}
    art_cache: dict[str, dict[str, bytes]] = {}
    aliases: dict[str, dict[str, str]] = {}

    for api_stem, set_code in SM_SETS.items():
        for card in loaded[api_stem]:
            slot = maps[api_stem][str(card["id"])]
            path = print_scripts.get((set_code, slot))
            if path is not None and fix_text(card.get("supertype", "")).startswith("Pok"):
                signatures.setdefault(mechanics_signature(card), module_for(path))

    for api_stem, set_code in SM_SETS.items():
        if selected and api_stem not in selected and set_code.lower() not in selected:
            continue
        cards = loaded[api_stem]
        slots = maps[api_stem]
        counts[set_code] = max(
            counts.get(set_code, 0), max(slots.values(), default=0)
        )
        by_name = {fix_text(card.get("name", "")): card for card in cards
                   if fix_text(card.get("supertype", "")).startswith("Pok")}
        scripts_dir = ROOT / "spirit" / "game" / "scripts" / "cards" / set_code
        assets_dir = ROOT / "spirit" / "assets" / "cards" / set_code
        scripts_dir.mkdir(parents=True, exist_ok=True)
        assets_dir.mkdir(parents=True, exist_ok=True)

        available = art_cache.get(set_code)
        if available is None:
            available = {}
            archive_path = _archive_for(source, set_code)
            if archive_path:
                with zipfile.ZipFile(archive_path) as archive:
                    # Ready PNG archives are lossless and take precedence.
                    available = _archive_entries(archive)
            # Late expansions and late promos only exist in the Unity cache.
            # For ready image archives, consult it solely when the archive is
            # incomplete instead of decoding duplicate textures.
            if not archive_path or len(available) < len(cards):
                cached = _cache_entries(source, set_code)
                for key, payload in cached.items():
                    available.setdefault(key, payload)
            art_cache[set_code] = available

        for original in cards:
            card = dict(original)
            slot = slots[str(card["id"])]
            card["number"] = str(slot)
            name = fix_text(card.get("name", "Unknown"))
            card["name"] = name
            stem = f"{clean_name(name)}_{slot}"
            script_path = scripts_dir / f"{stem}.py"
            card_guid = guid_for(str(original.get("id") or f"{set_code}-{slot}"))
            registered = guid_scripts.get(card_guid.lower()) or print_scripts.get((set_code, slot))
            asset_stem = registered.stem if registered is not None and registered.parent == scripts_dir else stem
            asset_path = assets_dir / f"{asset_stem}.png"
            supertype = fix_text(card.get("supertype", ""))
            kind = "pokemon" if supertype.startswith("Pok") else supertype.lower()

            if registered is not None or script_path.exists():
                skipped += 1
            else:
                base_module = None
                if kind == "pokemon":
                    base_module = signatures.get(mechanics_signature(original))
                elif kind in ("trainer", "energy"):
                    base_module = named_modules.get((kind, name))
                if base_module:
                    text = render_reprint(card, set_code, base_module)
                    reprints += 1
                elif kind == "pokemon":
                    text = render_pokemon(card, set_code, by_name)
                elif kind == "trainer":
                    text = render_trainer(card, set_code)
                elif kind == "energy":
                    text = render_energy(card, energy_profile(original), set_code)
                else:
                    raise ValueError(f"Unknown supertype {supertype!r} for {set_code}/{slot}")
                script_path.write_text(text, encoding="utf-8")
                guid_scripts[card_guid.lower()] = script_path
                print_scripts[(set_code, slot)] = script_path
                created += 1
                if kind == "pokemon":
                    signatures.setdefault(mechanics_signature(original), module_for(script_path))
                else:
                    named_modules.setdefault((kind, name), module_for(script_path))

            art_key = None if api_stem == "sma" else _variant_key(original, available)
            if art_key and not str(original.get("number") or "").isdigit() \
                    and not re.fullmatch(r"SM\d+", str(original.get("number") or ""), re.I):
                aliases.setdefault(set_code, {})[str(slot)] = art_key
            payload = available.get(art_key) if art_key else None
            if payload is not None:
                if not asset_path.exists() or asset_path.read_bytes() != payload:
                    asset_path.write_bytes(payload)
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
                elif not asset_path.exists():
                    art_missing += 1

        print(f"{api_stem:6} -> {set_code:9}: {len(cards):3} cards")

    for code, mapping in aliases.items():
        path = ROOT / "spirit" / "assets" / "cards" / code / "foil_aliases.json"
        path.write_text(json.dumps(mapping, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    _metadata(counts)
    print(
        f"Scripts created: {created} ({reprints} linked reprints); existing: {skipped}; "
        f"art updated: {art_written}; missing art: {art_missing}"
    )


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("sets", nargs="*", help="Optional API stem or server set code")
    parser.add_argument("--source", help="PTCGO source directory")
    parser.add_argument("--download-missing", action="store_true")
    args = parser.parse_args()
    run(
        {value.lower() for value in args.sets},
        source_directory(args.source).resolve(),
        args.download_missing,
    )


if __name__ == "__main__":
    main()
