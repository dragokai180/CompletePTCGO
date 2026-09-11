"""Build the compact per-print PTCGO foil table used by the server.

The archived Rotom export contains the original archetype attributes for every
PTCGO printing.  We retain the selected printing's primary and secondary foil
effects, mask, intensity and full-art flag, keyed by set and collector number.

Usage::

    python -m spirit.tools.sync_foil_metadata
"""
from __future__ import annotations

import json
from pathlib import Path
from urllib.parse import urljoin
from urllib.request import Request, urlopen

from spirit.game.foil_corrections import apply_foil_corrections


INDEX_URL = "https://malie.io/static/metamon/rotom.v4.json"
OUTPUT_PATH = Path(__file__).parents[1] / "game" / "foil_metadata.json"

# Repository/API set codes which differ from the PTCGO asset identifiers.
SET_ALIASES = {
    "Ann25th": "CEL25",
    "Ann25thR": "CEL25C",
    "CP": "SWSH35",
    "SF": "SWSH45",
    "PROMO_BW": "BWP",
    "Promo_XY": "XYP",
    "Promo_SM": "SMP",
    "Promo_SWSH": "SWSHP",
}


def _read_json(url: str) -> dict:
    request = Request(url, headers={"User-Agent": "CompletePTCGO/foil-metadata-sync"})
    with urlopen(request, timeout=60) as response:
        return json.load(response)


def _collector_key(value) -> str | None:
    if isinstance(value, bool) or value is None:
        return None
    try:
        return str(int(value))
    except (TypeError, ValueError):
        value = str(value).strip()
        return value or None


def _candidate_score(attributes: dict) -> tuple:
    """Prefer the normal card over reverse-holo and alternate print records."""
    mask = attributes.get("200620")
    variant = attributes.get("10020")
    has_primary_foil = mask not in (None, "None", "Reverse")
    return (
        mask == "Reverse",
        variant is not None,
        not has_primary_foil,
        str(variant or ""),
    )


def _compact_record(attributes: dict):
    effect = attributes.get("200610")
    mask = attributes.get("200620")
    # Preserve a normal non-holographic printing explicitly so it remains
    # distinguishable from a card that is absent from the imported catalog.
    if effect in (None, "None") or mask in (None, "None", "Reverse"):
        return None
    record = {
        "effect": effect,
        "mask": mask,
        "intensity": int(attributes.get("202080", 201)),
        "full_art": bool(attributes.get("201000", False)),
    }
    # Sword & Shield secret/full-art treatments combine their primary material
    # with a second client material.  Attribute 200611 is already a JSON list
    # in Rotom and must retain its order for CardImageRenderer.
    additional_effects = attributes.get("200611") or []
    if not isinstance(additional_effects, list):
        additional_effects = [additional_effects]
    additional_effects = [
        value for value in additional_effects if value is not None
    ]
    if additional_effects:
        record["effects"] = additional_effects
    return record


def build_metadata() -> dict:
    root = _read_json(INDEX_URL)
    version_path = root["versions"]["-1"]
    version_url = urljoin(INDEX_URL, version_path)
    version = _read_json(version_url)
    base_url = urljoin(version_url, "./")

    output = {}
    for set_code, descriptor in sorted(version["decks"].items()):
        deck = _read_json(urljoin(base_url, descriptor["deck"]))
        candidates = {}
        for row in deck.get("data", []):
            attributes = row.get("arch", {}).get("attributes", {})
            if attributes.get("200300") not in ("Pokemon", "TrainerCard", "Energy"):
                continue
            number = _collector_key(attributes.get("200780"))
            if number is None:
                continue
            candidates.setdefault(number, []).append(attributes)

        cards = {
            number: _compact_record(min(records, key=_candidate_score))
            for number, records in sorted(
                candidates.items(),
                key=lambda item: (not item[0].isdigit(), int(item[0]) if item[0].isdigit() else item[0]),
            )
        }
        if cards:
            output[set_code.upper()] = cards
            alias = SET_ALIASES.get(set_code)
            if alias:
                output[alias.upper()] = cards

    return apply_foil_corrections(output)


def main() -> None:
    metadata = build_metadata()
    OUTPUT_PATH.write_text(
        json.dumps(metadata, ensure_ascii=False, separators=(",", ":")),
        encoding="utf-8",
    )
    card_count = sum(len(cards) for cards in metadata.values())
    foil_count = sum(value is not None for cards in metadata.values() for value in cards.values())
    layered_count = sum(
        bool(value and value.get("effects"))
        for cards in metadata.values()
        for value in cards.values()
    )
    print(
        f"Wrote {card_count} print records ({foil_count} foil, "
        f"{layered_count} layered) to {OUTPUT_PATH}"
    )


if __name__ == "__main__":
    main()
