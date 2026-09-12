"""Download missing Sword & Shield, Scarlet & Violet, and Mega artwork.

This installer is intentionally limited to artwork.  It never creates or
modifies card definitions, so it is safe to run on a clean CompletePTCGO
checkout after the cbrew bundles have been imported.

Run from the repository root::

    python -m spirit.tools.install_recent_card_art

Pass ``swsh``, ``sv``, or ``mega`` to limit the download to one era::

    python -m spirit.tools.install_recent_card_art mega
"""

from __future__ import annotations

import argparse
import json
import os
from collections import OrderedDict
from concurrent.futures import ThreadPoolExecutor, as_completed
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable

import requests


ROOT = Path(__file__).resolve().parents[2]
DATA_ROOT = (
    ROOT / "tools" / "card-builder" / "data" /
    "pokemon-tcg-data" / "cards" / "en"
)
SCRIPTS_ROOT = ROOT / "spirit" / "game" / "scripts" / "cards"
ASSETS_ROOT = ROOT / "spirit" / "assets" / "cards"


@dataclass(frozen=True)
class RecentSet:
    era: str
    data_stem: str
    set_code: str


RECENT_SETS = OrderedDict(
    (entry.data_stem, entry)
    for entry in (
        RecentSet("swsh", "swsh1", "SWSH1"),
        RecentSet("swsh", "swsh2", "SWSH2"),
        RecentSet("swsh", "swsh3", "SWSH3"),
        RecentSet("swsh", "swsh35", "SWSH35"),
        RecentSet("swsh", "swsh4", "SWSH4"),
        RecentSet("swsh", "swsh45", "SWSH45"),
        RecentSet("swsh", "swsh5", "SWSH5"),
        RecentSet("swsh", "swsh6", "SWSH6"),
        RecentSet("swsh", "swsh7", "SWSH7"),
        RecentSet("swsh", "cel25", "CEL25"),
        RecentSet("swsh", "swsh8", "SWSH8"),
        RecentSet("swsh", "swsh9", "SWSH9"),
        RecentSet("swsh", "swsh10", "SWSH10"),
        RecentSet("swsh", "pgo", "PGO"),
        RecentSet("swsh", "swsh11", "SWSH11"),
        RecentSet("swsh", "swsh12", "SWSH12"),
        RecentSet("swsh", "swsh12pt5", "CZ"),
        RecentSet("sv", "sve", "SVE"),
        RecentSet("sv", "sv1", "SV1"),
        RecentSet("sv", "sv2", "SV2"),
        RecentSet("sv", "sv3", "SV3"),
        RecentSet("sv", "sv3pt5", "SV035"),
        RecentSet("sv", "sv4", "SV4"),
        RecentSet("sv", "sv4pt5", "SV045"),
        RecentSet("sv", "sv5", "SV05"),
        RecentSet("sv", "sv6", "SV06"),
        RecentSet("sv", "sv6pt5", "SV065"),
        RecentSet("sv", "sv7", "SV07"),
        RecentSet("sv", "sv8", "SV08"),
        RecentSet("sv", "sv8pt5", "SV085"),
        RecentSet("sv", "sv9", "SV09"),
        RecentSet("sv", "sv10", "SV10"),
        RecentSet("sv", "rsv10pt5", "RSV10PT5"),
        RecentSet("sv", "zsv10pt5", "ZSV10PT5"),
        RecentSet("sv", "svp", "SVP"),
        RecentSet("mega", "me1", "ME1"),
        RecentSet("mega", "me2", "ME2"),
        RecentSet("mega", "me2pt5", "ME2PT5"),
        RecentSet("mega", "me3", "ME3"),
        RecentSet("mega", "me4", "ME4"),
        RecentSet("mega", "me5", "ME5"),
        RecentSet("mega", "mep", "MEP"),
    )
)

# The upstream metadata currently points this print at a missing object.
IMAGE_OVERRIDES = {
    "svp-102": "https://pkmncards.com/wp-content/uploads/svbsp_en_102_std.png",
}


def normalize_collector_number(value: object) -> str:
    text = str(value or "").strip().lower()
    if text.isdigit():
        return str(int(text))
    return text


def collector_number_from_script(path: Path) -> str | None:
    _name, separator, number = path.stem.rpartition("_")
    if not separator or not number:
        return None
    return normalize_collector_number(number)


def mega_promo_url(number: str) -> str:
    """Return the English high-resolution Limitless URL for a Mega promo."""
    if not number.isdigit():
        raise ValueError(f"Unsupported Mega promo collector number: {number!r}")
    padded = f"{int(number):03d}"
    return (
        "https://limitlesstcg.nyc3.cdn.digitaloceanspaces.com/"
        f"tpci/MEP/MEP_{padded}_R_EN.png"
    )


def load_image_urls(card_set: RecentSet) -> dict[str, str]:
    data_path = DATA_ROOT / f"{card_set.data_stem}.json"
    if not data_path.exists():
        # pokemon-tcg-data does not yet ship a Mega promo catalog.  The promo
        # archive follows Limitless' stable English collector-number scheme.
        if card_set.data_stem == "mep":
            return {}
        raise FileNotFoundError(f"Missing bundled card catalog: {data_path}")

    payload = json.loads(data_path.read_text(encoding="utf-8"))
    if not isinstance(payload, list):
        raise ValueError(f"Expected a card list in {data_path}")

    result: dict[str, str] = {}
    for card in payload:
        number = normalize_collector_number(card.get("number"))
        card_id = str(card.get("id") or "").lower()
        url = IMAGE_OVERRIDES.get(card_id) or (card.get("images") or {}).get("large")
        if number and url:
            result[number] = str(url)
    return result


def image_url(card_set: RecentSet, number: str, known: dict[str, str]) -> str:
    if number in known:
        return known[number]
    if card_set.data_stem == "mep":
        return mega_promo_url(number)
    # This also covers promo prints added after the bundled metadata snapshot.
    return f"https://images.pokemontcg.io/{card_set.data_stem}/{number}_hires.png"


def selected_sets(values: Iterable[str]) -> list[RecentSet]:
    requested = {value.strip().lower() for value in values if value.strip()}
    if not requested or "all" in requested:
        return list(RECENT_SETS.values())

    aliases = {
        "sword-shield": "swsh",
        "sword-and-shield": "swsh",
        "sword_and_shield": "swsh",
        "scarlet-violet": "sv",
        "scarlet_and_violet": "sv",
        "mega-evolution": "mega",
        "mega_evolution": "mega",
    }
    requested = {aliases.get(value, value) for value in requested}
    matches = [
        card_set for card_set in RECENT_SETS.values()
        if card_set.era in requested
        or card_set.data_stem in requested
        or card_set.set_code.lower() in requested
    ]
    unmatched = requested - {
        value
        for value in requested
        if any(
            value in (entry.era, entry.data_stem, entry.set_code.lower())
            for entry in RECENT_SETS.values()
        )
    }
    if unmatched:
        raise ValueError("Unknown era or set: " + ", ".join(sorted(unmatched)))
    return matches


def build_tasks(
    card_set: RecentSet,
    *,
    overwrite: bool = False,
) -> list[tuple[str, Path]]:
    scripts_dir = SCRIPTS_ROOT / card_set.set_code
    if not scripts_dir.exists():
        return []

    known = load_image_urls(card_set)
    tasks: list[tuple[str, Path]] = []
    for script_path in sorted(scripts_dir.glob("*.py")):
        if script_path.name == "__init__.py":
            continue
        number = collector_number_from_script(script_path)
        if number is None:
            continue
        destination = ASSETS_ROOT / card_set.set_code / f"{script_path.stem}.png"
        if destination.exists() and not overwrite:
            continue
        tasks.append((image_url(card_set, number, known), destination))
    return tasks


def download_one(task: tuple[str, Path]) -> tuple[bool, str]:
    url, destination = task
    destination.parent.mkdir(parents=True, exist_ok=True)
    temporary = destination.with_suffix(".png.part")
    try:
        response = requests.get(
            url,
            timeout=45,
            headers={"User-Agent": "CompletePTCGO/recent-card-art-installer"},
        )
        response.raise_for_status()
        if not response.content.startswith(b"\x89PNG\r\n\x1a\n"):
            raise ValueError("response was not a PNG")
        temporary.write_bytes(response.content)
        os.replace(temporary, destination)
        return True, str(destination)
    except Exception as exc:  # diagnostics belong in command output
        temporary.unlink(missing_ok=True)
        return False, f"{url}: {exc}"


def run(values: Iterable[str], workers: int, overwrite: bool) -> None:
    sets = selected_sets(values)
    tasks: list[tuple[str, Path]] = []
    for card_set in sets:
        set_tasks = build_tasks(card_set, overwrite=overwrite)
        tasks.extend(set_tasks)
        print(
            f"{card_set.set_code:10} "
            f"missing artwork: {len(set_tasks)}"
        )

    if not tasks:
        print("All selected card artwork is already installed.")
        return

    failures: list[str] = []
    completed = 0
    with ThreadPoolExecutor(max_workers=max(1, workers)) as pool:
        futures = [pool.submit(download_one, task) for task in tasks]
        for future in as_completed(futures):
            ok, detail = future.result()
            completed += 1
            if not ok:
                failures.append(detail)
            if completed % 100 == 0 or completed == len(futures):
                print(
                    f"Artwork: {completed}/{len(futures)} "
                    f"({len(failures)} failures)"
                )

    if failures:
        print("Artwork download failures:")
        for failure in failures:
            print("  " + failure)
        raise SystemExit(2)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "eras_or_sets",
        nargs="*",
        help="Optional era (swsh, sv, or mega), data stem, or server set code",
    )
    parser.add_argument("--workers", type=int, default=20)
    parser.add_argument("--overwrite", action="store_true")
    args = parser.parse_args()
    try:
        run(args.eras_or_sets, args.workers, args.overwrite)
    except (FileNotFoundError, ValueError) as exc:
        parser.error(str(exc))


if __name__ == "__main__":
    main()
