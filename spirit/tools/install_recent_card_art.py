"""Download missing English card artwork from HGSS through Mega Evolution.

This installer is intentionally limited to artwork.  It never creates or
modifies card definitions, so it is safe to run on a clean CompletePTCGO
checkout with or without the optional cbrew bundles.

Run from the repository root::

    python -m spirit.tools.install_recent_card_art

Pass ``hgss``, ``bw``, ``xy``, ``sm``, ``swsh``, ``sv``, or ``mega``
to limit the download to one era::

    python -m spirit.tools.install_recent_card_art mega
"""

from __future__ import annotations

import argparse
import io
import json
import os
import re
import tempfile
from collections import OrderedDict
from concurrent.futures import ThreadPoolExecutor, as_completed
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable

import requests
from PIL import Image
from spirit.game.gallery_catalog import GALLERY_SETS, gallery_number


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
        RecentSet("bw", "free_energy", "Free_Energy"),
        *(RecentSet("hgss", f"hgss{i}", f"HGSS{i}") for i in range(1, 5)),
        RecentSet("hgss", "hsp", "Promo_HGSS"),
        RecentSet("hgss", "col1", "COL"),
        *(RecentSet("bw", f"bw{i}", f"BW{i}") for i in range(1, 12)),
        RecentSet("bw", "bwp", "PROMO_BW"),
        RecentSet("bw", "dv1", "DV"),
        *(RecentSet("xy", f"xy{i}", f"XY{i}") for i in range(13)),
        RecentSet("xy", "xyp", "Promo_XY"),
        RecentSet("xy", "dc1", "TATM"),
        RecentSet("xy", "g1", "TwentiethAnn"),
        *(RecentSet("sm", f"sm{i}", f"SM{i}") for i in range(1, 13)),
        RecentSet("sm", "smp", "Promo_SM"),
        RecentSet("sm", "sm35", "SL"),
        RecentSet("sm", "sm75", "DM"),
        RecentSet("sm", "sm115", "HF"),
        RecentSet("sm", "det1", "GUM"),
        RecentSet("swsh", "swsh_energy", "SWSH_Energy"),
        RecentSet("swsh", "swshp", "Promo_SWSH"),
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
        RecentSet("mega", "me55", "ME55"),
        RecentSet("mega", "mee", "MEE"),
        RecentSet("mega", "mep", "MEP"),
    )
)

# The upstream metadata currently points this print at a missing object.
IMAGE_OVERRIDES = {
    "svp-102": "https://pkmncards.com/wp-content/uploads/svbsp_en_102_std.png",
}

# Unnumbered SUM basic Energy prints use type letters at Limitless. Slots
# 164..172 are internal catalog numbers, not printed collector numbers.
SM_BASIC_ENERGY_CODES = dict(zip(map(str, range(164, 173)), "GRWLPFDMY"))


def sm_basic_energy_url(card_set: RecentSet, number: str) -> str | None:
    code = SM_BASIC_ENERGY_CODES.get(number) if card_set.set_code == "SM1" else None
    if code is None:
        return None
    return ("https://limitlesstcg.nyc3.cdn.digitaloceanspaces.com/"
            f"tpci/SUM/SUM_{code}_R_EN.png")


def cropped_sm_basic_energy(card_set: RecentSet, number: str, path: Path) -> bool:
    """Repair the known cropped downloads without replacing native artwork."""
    if sm_basic_energy_url(card_set, number) is None:
        return False
    try:
        with Image.open(path) as picture:
            return picture.size == (700, 990)
    except (OSError, ValueError):
        return False

# Verified English unnumbered Energy scans. These sets have no upstream
# pokemon-tcg-data catalog; their internal numbers are NOT normal set numbers.
ENERGY_NAMES = (
    "grass", "fire", "water", "lightning", "psychic",
    "fighting", "darkness", "metal", "fairy",
)


def energy_image_urls(set_code: str) -> dict[str, str]:
    root = "https://pkmncards.com/wp-content/uploads/"
    if set_code == "SWSH_Energy":
        return {
            str(n): root + f"en_US-SWSH_Energy-{n:03d}-{name}_energy."
            + ("jpg" if n <= 9 else "png")
            for n, name in enumerate(ENERGY_NAMES + ENERGY_NAMES[:8], 1)
        }
    return {
        str(n): root + f"en_US-{'XY' if name == 'fairy' else 'BW'}_Energy-"
        + f"{n:03d}-{name}_energy.png"
        for n, name in enumerate(ENERGY_NAMES, 1)
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


def load_catalog(data_stem: str) -> list[dict]:
    """Use a local snapshot when present, otherwise fetch the public catalog.

    card-builder/data is gitignored and is not guaranteed on a fresh checkout.
    Downloading metadata does not import artwork or assets from TCG Live.
    """
    path = DATA_ROOT / f"{data_stem}.json"
    if path.exists():
        payload = json.loads(path.read_text(encoding="utf-8"))
    else:
        response = requests.get(
            "https://raw.githubusercontent.com/PokemonTCG/pokemon-tcg-data/"
            f"master/cards/en/{data_stem}.json", timeout=45)
        response.raise_for_status()
        payload = response.json()
    if not isinstance(payload, list):
        raise ValueError(f"Expected a card list for {data_stem}")
    return payload


def load_image_urls(card_set: RecentSet) -> dict[str, str]:
    if card_set.set_code in ("SWSH_Energy", "Free_Energy"):
        return energy_image_urls(card_set.set_code)
    # These numbered Energy sets outgrow the PokemonTCG metadata snapshots.
    # Use the verified Scrydex print IDs directly, including anniversary MEE
    # 009-016 and SVE 017-024, without requiring a local/Live catalog.
    energy_count = {"MEE": 16, "SVE": 24}.get(card_set.set_code)
    if energy_count is not None:
        return {
            str(number): f"https://images.scrydex.com/pokemon/{card_set.data_stem}-{number}/large"
            for number in range(1, energy_count + 1)
        }
    data_path = DATA_ROOT / f"{card_set.data_stem}.json"
    if not data_path.exists():
        # pokemon-tcg-data does not yet ship a Mega promo catalog.  The promo
        # archive follows Limitless' stable English collector-number scheme.
        if card_set.data_stem == "mep":
            return {}
    payload = load_catalog(card_set.data_stem)
    if not isinstance(payload, list):
        raise ValueError(f"Expected a card list in {data_path}")

    # Use the importers' protocol numbering for promos and alternate prints.
    numbers = {}
    if card_set.era == "hgss":
        from spirit.tools.import_hgss_sets import internal_number
        numbers = {c["id"]: internal_number(c, card_set.data_stem) for c in payload}
    elif card_set.era == "xy":
        from spirit.tools.import_xy_sets import internal_number
        numbers = {c["id"]: internal_number(c, card_set.data_stem) for c in payload}
    elif card_set.era == "sm":
        from spirit.tools.import_sm_sets import number_map
        numbers = number_map(payload, card_set.data_stem)

    result: dict[str, str] = {}
    for card in payload:
        number = normalize_collector_number(numbers.get(card.get("id"), card.get("number")))
        if card_set.data_stem == "swshp":
            number = str(int(str(card["number"]).removeprefix("SWSH")))
        card_id = str(card.get("id") or "").lower()
        if card_set.era in ("sv", "mega") and card_id.startswith(card_set.data_stem + "-"):
            # Black Bolt #80 incorrectly repeats #60 in upstream metadata.
            number = normalize_collector_number(card_id[len(card_set.data_stem) + 1:])
        if card_set.data_stem == "me55" and card.get("number") in ("R", "G", "B"):
            from spirit.tools.import_thirtieth_celebration import RGB_NUMBERS
            number = str(RGB_NUMBERS[card["number"]])
        url = IMAGE_OVERRIDES.get(card_id) or (card.get("images") or {}).get("large")
        if number and url:
            result[number] = str(url)
    if card_set.data_stem == "sm115":
        # Shiny Vault shares HF's directory, with slots starting at 101.
        result.update(load_image_urls(RecentSet("sm", "sma", "HF")))
    # TG/GG prints belong to their parent set in the client's numeric catalog,
    # but the artwork provider uses a separate gallery ID and printed number.
    for gallery, (parent, _offset, _size) in GALLERY_SETS.items():
        if parent != card_set.set_code:
            continue
        for card in load_catalog(gallery):
            number = str(gallery_number(gallery, card["number"]))
            result[number] = card["images"]["large"]
    return result


def image_url(card_set: RecentSet, number: str, known: dict[str, str]) -> str:
    energy_url = sm_basic_energy_url(card_set, number)
    if energy_url:
        return energy_url
    if number in known:
        return known[number]
    if card_set.data_stem == "mep":
        return mega_promo_url(number)
    if card_set.data_stem == "swshp":
        return f"https://images.pokemontcg.io/swshp/SWSH{int(number):03d}_hires.png"
    # This also covers promo prints added after the bundled metadata snapshot.
    return f"https://images.pokemontcg.io/{card_set.data_stem}/{number}_hires.png"


def image_candidates(card_set: RecentSet, number: str, known: dict[str, str]) -> tuple[str, ...]:
    primary = image_url(card_set, number, known)
    urls = [primary]
    # Derive alternate identity from the printed URL, not internal numbering:
    # HGSS/XY promos and Shiny Vault use remapped protocol slots.
    match = re.fullmatch(r"https://images\.pokemontcg\.io/([^/]+)/(.+)_hires\.png", primary)
    if match:
        stem, printed = match.groups()
        urls.append(f"https://images.scrydex.com/pokemon/{stem}-{printed}/large")
    if card_set.data_stem == "svp":
        urls.append(
            "https://limitlesstcg.nyc3.cdn.digitaloceanspaces.com/"
            f"tpci/SVP/SVP_{int(number):03d}_R_EN.png")
    return tuple(dict.fromkeys(urls))


def selected_sets(values: Iterable[str]) -> list[RecentSet]:
    requested = {value.strip().lower() for value in values if value.strip()}
    if not requested or "all" in requested:
        return list(RECENT_SETS.values())

    aliases = {
        "black-and-white": "bw",
        "sun-moon": "sm",
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
) -> list[tuple[tuple[str, ...], Path]]:
    scripts_dir = SCRIPTS_ROOT / card_set.set_code
    if not scripts_dir.exists():
        return []

    known = load_image_urls(card_set)
    tasks: list[tuple[tuple[str, ...], Path]] = []
    for script_path in sorted(scripts_dir.glob("*.py")):
        if script_path.name == "__init__.py":
            continue
        number = collector_number_from_script(script_path)
        if number is None:
            continue
        destination = ASSETS_ROOT / card_set.set_code / f"{script_path.stem}.png"
        if (destination.exists() and not overwrite
                and not cropped_sm_basic_energy(card_set, number, destination)):
            continue
        tasks.append((image_candidates(card_set, number, known), destination))
    return tasks


def download_one(task: tuple[str | tuple[str, ...], Path]) -> tuple[bool, str]:
    candidates, destination = task
    urls = (candidates,) if isinstance(candidates, str) else candidates
    destination.parent.mkdir(parents=True, exist_ok=True)
    errors = []
    for url in urls:
        temporary = None
        try:
            with requests.get(
                url, timeout=45,
                headers={"User-Agent": "CompletePTCGO/card-art-installer"},
            ) as response:
                response.raise_for_status()
                payload = response.content
            # Some English Energy scans are JPEG. Validate/decode instead of
            # trusting the extension or accepting an HTML error as artwork.
            with Image.open(io.BytesIO(payload)) as picture:
                picture.load()
                if picture.format not in ("PNG", "JPEG", "WEBP"):
                    raise ValueError("unsupported image format")
                if picture.format != "PNG":
                    output = io.BytesIO()
                    picture.convert("RGBA").save(output, format="PNG")
                    payload = output.getvalue()
            fd, name = tempfile.mkstemp(suffix=".part", dir=destination.parent)
            temporary = Path(name)
            with os.fdopen(fd, "wb") as output:
                output.write(payload)
            os.replace(temporary, destination)
            return True, str(destination)
        except Exception as exc:
            errors.append(f"{url}: {exc}")
        finally:
            if temporary is not None:
                temporary.unlink(missing_ok=True)
    return False, f"{destination}: " + "; ".join(errors)


def install_native_energy(overwrite: bool, source: str | None = None) -> list[str]:
    """Restore both SWSH basic Energy series from cbrew, without guessed URLs."""
    from spirit.tools.ptcgo_local_assets import install_card_art

    failures = []
    scripts = sorted((SCRIPTS_ROOT / "SWSH_Energy").glob("*.py"))
    if len(scripts) != 17:
        return ["SWSH_Energy: expected 17 card definitions; update the checkout."]
    restored = 0
    for script in scripts:
        destination = ASSETS_ROOT / "SWSH_Energy" / f"{script.stem}.png"
        if destination.is_file() and not overwrite:
            continue
        number = collector_number_from_script(script)
        if install_card_art("SWSH_Energy", number, destination,
                            source=source, overwrite=overwrite):
            restored += 1
        else:
            failures.append(
                f"SWSH_Energy/{script.stem}: original texture unavailable. "
                "Use --cbrew-source or PTCGO_ART_SOURCE_DIR to select the "
                "cbrew folder containing BW Cache.zip / SM Cache.zip."
            )
    print(f"SWSH_Energy: {restored} original textures restored; {len(failures)} missing.")
    return failures


def restore_native_promos(source: str) -> None:
    """Prefer available cbrew textures, retaining downloads for cache gaps."""
    from spirit.tools.ptcgo_local_assets import install_card_art
    restored = 0
    for script in (SCRIPTS_ROOT / 'Promo_SWSH').glob('*.py'):
        number = collector_number_from_script(script)
        if number is not None and install_card_art(
                'Promo_SWSH', number, ASSETS_ROOT / 'Promo_SWSH' / (script.stem + '.png'),
                source=source, overwrite=True):
            restored += 1
    from spirit.game.vunion import SPECS
    for name, spec in SPECS.items():
        start = spec[0]
        install_card_art('Promo_SWSH', f'{start}to{start + 3}',
                         ASSETS_ROOT / 'Promo_SWSH' / f'{name}VUNION_combined.png', source=source, overwrite=True)
    install_card_art('Promo_SWSH', '287to290',
                     ASSETS_ROOT / 'Promo_SWSH' / 'MorpekoVUNION_alternate_combined.png', source=source, overwrite=True)
    print(f'Promo_SWSH: {restored} original cbrew textures restored.')


def assemble_downloaded_vunion_faces() -> list[str]:
    """Build missing complete faces from four downloaded quadrants, never foils.

    Keep original cbrew composites when present. The alternate Morpeko art
    has its own asset, independent of the original 215-218 printing.
    """
    from spirit.game.vunion import SPECS
    groups = [(name, spec[0], 'combined') for name, spec in SPECS.items()]
    groups.append(('Morpeko', 287, 'alternate_combined'))
    errors = []
    for name, start, suffix in groups:
        folder = ASSETS_ROOT / 'Promo_SWSH'
        target = folder / f'{name}VUNION_{suffix}.png'
        if target.is_file():
            continue
        stems = [f'{name}VUNION_{n}' for n in range(start, start + 4)]
        if not all((SCRIPTS_ROOT / 'Promo_SWSH' / (s + '.py')).is_file() for s in stems):
            continue
        try:
            parts = []
            for stem in stems:
                with Image.open(folder / (stem + '.png')) as picture:
                    parts.append(picture.convert('RGB'))
            width, height = parts[0].size
            if any(p.size != (width, height) for p in parts):
                raise ValueError('quadrant dimensions differ')
            combined = Image.new('RGB', (width * 2, height * 2))
            for slot, part in enumerate(parts):
                combined.paste(part, ((slot % 2) * width, (slot // 2) * height))
            combined.save(target)
        except (OSError, ValueError) as exc:
            errors.append(f'V-UNION {name}/{start}: {exc}')
    return errors


def run(values: Iterable[str], workers: int, overwrite: bool,
        cbrew_source: str | None = None) -> None:
    sets = selected_sets(values)
    tasks: list[tuple[tuple[str, ...], Path]] = []
    failures: list[str] = []
    for card_set in sets:
        if card_set.set_code == 'Promo_SWSH' and cbrew_source:
            restore_native_promos(cbrew_source)
        if card_set.set_code == "SWSH_Energy" and cbrew_source:
            missing = install_native_energy(overwrite, cbrew_source)
            if missing:
                print("SWSH_Energy: downloading missing textures from English scans.")
        try:
            set_tasks = build_tasks(
                card_set,
                overwrite=overwrite and not (card_set.set_code == "SWSH_Energy" and cbrew_source),
            )
        except (FileNotFoundError, ValueError) as exc:
            failures.append(f"{card_set.set_code}: {exc}")
            continue
        tasks.extend(set_tasks)
        print(
            f"{card_set.set_code:10} "
            f"missing artwork: {len(set_tasks)}"
        )

    if not tasks and not failures:
        if any(s.set_code == 'Promo_SWSH' for s in sets):
            errors = assemble_downloaded_vunion_faces()
            if errors:
                raise ValueError('; '.join(errors))
        print("All selected card artwork is already installed.")
        return

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

    if any(s.set_code == 'Promo_SWSH' for s in sets):
        failures.extend(assemble_downloaded_vunion_faces())
    if failures:
        print("Artwork installation failures:")
        for failure in failures:
            print("  " + failure)
        raise SystemExit(2)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "eras_or_sets",
        nargs="*",
        help="Optional era (hgss, bw, xy, sm, swsh, sv, mega), data stem, or server set code",
    )
    parser.add_argument("--workers", type=int, default=20)
    parser.add_argument("--overwrite", action="store_true")
    parser.add_argument("--cbrew-source", help="Native source for SWSH Energy and promos; missing textures are downloaded")
    args = parser.parse_args()
    try:
        run(args.eras_or_sets, args.workers, args.overwrite, args.cbrew_source)
    except (FileNotFoundError, ValueError) as exc:
        parser.error(str(exc))


if __name__ == "__main__":
    main()
