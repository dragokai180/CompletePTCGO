"""Import original artwork from a local Pokemon TCG Online asset collection.

The Spriters Resource archives stored next to a PTCGO cache contain the native
1024x1024 card textures used by the Unity client.  They are preferred over web
API renders whenever the requested set is available.  The same local folder can
also restore the original home/landing, loading-background, logo and set-icon
AssetBundles without copying the multi-gigabyte card cache into the project.

Run from the repository root::

    python -m spirit.tools.ptcgo_local_assets --source C:\\path\\to\\PTCGO
"""

from __future__ import annotations

import argparse
import io
import os
import re
import tempfile
import zipfile
from functools import lru_cache
from pathlib import Path, PurePosixPath

import UnityPy
from spirit.game.excluded_prints import excluded_print


PROJECT_DIR = Path(__file__).resolve().parents[2]
CARD_SCRIPT_DIR = PROJECT_DIR / "spirit" / "game" / "scripts" / "cards"
CARD_ASSET_DIR = PROJECT_DIR / "spirit" / "assets" / "cards"
EXTERNAL_CACHE_DIR = PROJECT_DIR / "spirit" / "assets" / "externalCache"

DEFAULT_SOURCE_DIR = Path("A:/PTCGO")
SOURCE_ENV = "PTCGO_ART_SOURCE_DIR"

# Printed RC numbers differ from the numeric texture slots in native bundles.
RADIANT_COLLECTIONS = {"BW11": (115, 25), "TWENTIETHANN": (100, 32)}


def _native_collector(set_code: str, value: object) -> object:
    match = re.fullmatch(r"RC0*(\d+)", str(value).strip(), re.IGNORECASE)
    layout = RADIANT_COLLECTIONS.get(set_code.upper())
    if match and layout and 1 <= int(match.group(1)) <= layout[1]:
        return layout[0] + int(match.group(1))
    return value


# Exact archive titles avoid confusing identically named promo archives from
# different eras.  Additional entries are useful when their scripts are added
# later: the importer will simply ignore a set which is not implemented yet.
CARD_ARCHIVES = {
    "PROMO_HGSS": "HeartGold & SoulSilver Series - Black Star Promos.zip",
    "HGSS1": "HeartGold & SoulSilver Series - HeartGold & SoulSilver.zip",
    "HGSS2": "HeartGold & SoulSilver Series - Unleashed.zip",
    "HGSS3": "HeartGold & SoulSilver Series - Undaunted.zip",
    "HGSS4": "HeartGold & SoulSilver Series - Triumphant.zip",
    "COL": "HeartGold & SoulSilver Series - Call of Legends.zip",
    "BW1": "Black & White Series - Black & White.zip",
    "PROMO_BW": "Black & White Series - Black Star Promos.zip",
    "BW3": "Black & White Series - Noble Victories.zip",
    "BW4": "Black & White Series - Next Destinies.zip",
    "BW5": "Black & White Series - Dark Explorers.zip",
    "DV": "Black & White Series - Dragon Vault.zip",
    "BW7": "Black & White Series - Boundaries Crossed.zip",
    "BW8": "Black & White Series - Plasma Storm.zip",
    "BW9": "Black & White Series - Plasma Freeze.zip",
    "BW10": "Black & White Series - Plasma Blast.zip",
    "BW11": "Black & White Series - Legendary Treasures.zip",
    "XY0": "XY Series - Kalos Starter Set.zip",
    "XY1": "XY Series - XY.zip",
    "XY2": "XY Series - Flashfire.zip",
    "XY3": "XY Series - Furious Fists.zip",
    "XY4": "XY Series - Phantom Forces.zip",
    "XY5": "XY Series - Primal Clash.zip",
    "TATM": "XY Series - Double Crisis.zip",
    "XY6": "XY Series - Roaring Skies.zip",
    "XY7": "XY Series - Ancient Origins.zip",
    "XY8": "XY Series - BREAKthrough.zip",
    "XY9": "XY Series - BREAKpoint.zip",
    "TWENTIETHANN": "XY Series - Generations.zip",
    "XY10": "XY Series - Fates Collide.zip",
    "XY11": "XY Series - Steam Siege.zip",
    "XY12": "XY Series - Evolutions.zip",
    "PROMO_XY": "XY Series - Black Star Promos.zip",
    "SM1": "Sun & Moon Series - Sun & Moon.zip",
    "SM2": "Sun & Moon Series - Guardians Rising.zip",
    "SM3": "Sun & Moon Series - Burning Shadows.zip",
    "SL": "Sun & Moon Series - Shining Legends.zip",
    "SM4": "Sun & Moon Series - Crimson Invasion.zip",
    "SM5": "Sun & Moon Series - Ultra Prism.zip",
    "SM6": "Sun & Moon Series - Forbidden Light.zip",
    "SM7": "Sun & Moon Series - Celestial Storm.zip",
    "DM": "Sun & Moon Series - Dragon Majesty.zip",
    "SM8": "Sun & Moon Series - Lost Thunder.zip",
    "SM9": "Sun & Moon Series - Team Up.zip",
    "PROMO_SM": "Sun & Moon Series - Black Star Promos.zip",
}

_PROMO_SET_PREFIX = {
    "PROMO_HGSS": "HGSS",
    "PROMO_BW": "BW",
    "PROMO_XY": "XY",
    "PROMO_SM": "SM",
}

_LANDING_PAGE_NAMES = (
    "swsh10_palkia_landingpage",
    "swsh10_typhlosion_landingpage",
    "swsh10_decidueye_landingpage",
    "swsh10_dialga_landingpage",
    "swsh10_samurott_landingpage",
)

_LANDING_PAGE_TITLES = (
    "Astral Radiance — Palkia",
    "Astral Radiance — Hisuian Typhlosion",
    "Astral Radiance — Hisuian Decidueye",
    "Astral Radiance — Dialga",
    "Astral Radiance — Hisuian Samurott",
)


def source_directory(value: str | os.PathLike | None = None) -> Path:
    """Resolve the configured PTCGO artwork directory."""
    configured = value or os.environ.get(SOURCE_ENV)
    return Path(configured).expanduser() if configured else DEFAULT_SOURCE_DIR


def _find_archive(source: Path, suffix: str) -> Path | None:
    matches = sorted(
        path
        for path in source.glob(f"*{suffix}")
        if not path.name.endswith(" (1).zip")
    )
    return matches[0] if matches else None


def _collector_from_script(set_code: str, stem: str) -> int | None:
    radiant = re.search(r"_(RC\d+)$", stem, re.IGNORECASE)
    if radiant:
        value = _native_collector(set_code, radiant.group(1))
        return value if isinstance(value, int) else None
    promo_prefix = _PROMO_SET_PREFIX.get(set_code)
    pattern = rf"_{promo_prefix}(\d+)$" if promo_prefix else r"_(\d+)$"
    match = re.search(pattern, stem, re.IGNORECASE)
    return int(match.group(1)) if match else None


def _collector_value(value: object) -> int | None:
    text = str(value or "").strip()
    if text.upper().startswith("RC"):
        return None
    match = re.search(r"(\d+)$", text)
    return int(match.group(1)) if match else None


def _collector_key(value: object) -> str | None:
    """Canonical key shared by script collector values and Unity asset names."""
    text = str(value or "").strip().upper()
    radiant = re.fullmatch(r"RC0*(\d+)", text)
    if radiant:
        return f"RC{int(radiant.group(1))}"
    number = _collector_value(text)
    return str(number) if number is not None else None


def _collector_key_from_script(set_code: str, stem: str) -> str | None:
    radiant = re.search(r"_RC(\d+)$", stem, re.IGNORECASE)
    if radiant:
        return str(_native_collector(set_code, f"RC{int(radiant.group(1))}"))
    number = _collector_from_script(set_code, stem)
    return str(number) if number is not None else None


def _archive_card_entries(archive: zipfile.ZipFile) -> dict[int, str]:
    """Return native main-set card textures, excluding pips/foil helpers."""
    entries: dict[int, str] = {}
    gold_entries: dict[int, str] = {}
    for name in archive.namelist():
        path = PurePosixPath(name)
        if path.suffix.lower() != ".png" or len(path.parts) != 2:
            continue
        if path.stem.isdigit():
            entries[int(path.stem)] = name
            continue
        gold = re.fullmatch(r"(\d+)_gold", path.stem, re.IGNORECASE)
        if gold:
            gold_entries[int(gold.group(1))] = name
    for number, name in gold_entries.items():
        entries.setdefault(number, name)
    return entries


def _cache_archives(source: Path) -> list[Path]:
    # The SM snapshot contains the newest sets, while the BW snapshot retains
    # several older bundles that had already been evicted from the later cache.
    return [
        path
        for path in (source / "SM Cache.zip", source / "BW Cache.zip")
        if path.is_file()
    ]


def _installer_set_bundles(
    source: Path, set_code: str
) -> list[tuple[zipfile.ZipFile, zipfile.ZipInfo]]:
    """Native set bundles shipped directly in the retired PTCGO installer.

    The downloaded cache snapshots contain seven of the nine ``Free_Energy``
    bundles, but their Fire and Fairy directories are empty.  Both complete
    bundles still live under StreamingAssets in ``PTCGO Exe.zip``.  Keep this
    narrow to Free_Energy so ordinary set imports continue preferring the
    dedicated card archives/cache snapshots.
    """
    if set_code.casefold() != "free_energy":
        return []
    installer = source / "PTCGO Exe.zip"
    if not installer.is_file():
        return []
    archive = zipfile.ZipFile(installer)
    matches = []
    for info in archive.infolist():
        path = PurePosixPath(info.filename.replace("\\", "/"))
        if path.suffix.casefold() != ".unity3d":
            continue
        if _bundle_matches_set(path.stem, set_code):
            matches.append((archive, info))
    if not matches:
        archive.close()
    return matches


def _bundle_matches_set(bundle_name: str, set_code: str) -> bool:
    prefix = f"en_US_{set_code}_".casefold()
    lowered = bundle_name.casefold()
    return lowered.startswith(prefix) and "_wp_" not in lowered


def _texture_collector_key(name: str) -> str | None:
    text = str(name or "").strip().upper()
    if text.isdigit():
        return str(int(text))
    radiant = re.fullmatch(r"RC0*(\d+)", text)
    if radiant:
        return f"RC{int(radiant.group(1))}"
    gold = re.fullmatch(r"0*(\d+)_GOLD", text)
    if gold:
        return str(int(gold.group(1)))
    return None


@lru_cache(maxsize=2)
def _cached_set_art(source_text: str, set_code: str) -> dict[str, bytes]:
    """Decode locally cached native card textures for one set.

    Results are cached for the duration of an import_set process, so importing
    a full collection does not reopen and decode its Unity bundles per card.
    """
    source = Path(source_text)
    found: dict[str, bytes] = {}
    for cache_path in _cache_archives(source):
        with zipfile.ZipFile(cache_path) as archive:
            candidates = []
            for info in archive.infolist():
                if not info.filename.replace("\\", "/").endswith("/__data"):
                    continue
                bundle_name = _cache_bundle_name(info.filename)
                if bundle_name and _bundle_matches_set(bundle_name, set_code):
                    candidates.append(info)
            for info in candidates:
                try:
                    environment = UnityPy.load(archive.read(info))
                    for obj in environment.objects:
                        if obj.type.name != "Texture2D":
                            continue
                        texture = obj.read()
                        key = _texture_collector_key(texture.m_Name)
                        if key is None or key in found:
                            continue
                        if int(texture.m_Width) < 512 or int(texture.m_Height) < 512:
                            continue
                        output = io.BytesIO()
                        texture.image.convert("RGBA").save(output, format="PNG")
                        found[key] = output.getvalue()
                except Exception as exc:
                    print(f"[cards] could not inspect {info.filename}: {exc}")

    # Free_Energy Fire/Fairy were absent from both cache snapshots.  Complete
    # native bundles for all nine types are shipped in the original client.
    installer_matches = _installer_set_bundles(source, set_code)
    try:
        for archive, info in installer_matches:
            try:
                environment = UnityPy.load(archive.read(info))
                for obj in environment.objects:
                    if obj.type.name != "Texture2D":
                        continue
                    texture = obj.read()
                    key = _texture_collector_key(texture.m_Name)
                    if key is None or key in found:
                        continue
                    if int(texture.m_Width) < 512 or int(texture.m_Height) < 512:
                        continue
                    output = io.BytesIO()
                    texture.image.convert("RGBA").save(output, format="PNG")
                    found[key] = output.getvalue()
            except Exception as exc:
                print(f"[cards] could not inspect {info.filename}: {exc}")
    finally:
        for archive in {archive for archive, _ in installer_matches}:
            archive.close()
    return found


def _atomic_write(destination: Path, payload: bytes) -> None:
    destination.parent.mkdir(parents=True, exist_ok=True)
    fd, temp_name = tempfile.mkstemp(
        prefix=f".{destination.name}.", suffix=".tmp", dir=destination.parent
    )
    try:
        with os.fdopen(fd, "wb") as output:
            output.write(payload)
        os.replace(temp_name, destination)
    finally:
        try:
            os.unlink(temp_name)
        except FileNotFoundError:
            pass


def install_card_art(
    set_code: str,
    collector_number: object,
    destination: str | os.PathLike,
    source: str | os.PathLike | None = None,
    *,
    overwrite: bool = True,
) -> bool:
    """Install one native card texture; return False if no local art exists."""
    set_code = str(set_code).upper()
    if excluded_print(set_code, collector_number):
        return False
    collector_number = _native_collector(set_code, collector_number)
    suffix = CARD_ARCHIVES.get(set_code)
    number = _collector_value(collector_number)
    local_source = source_directory(source)
    destination = Path(destination)
    if destination.exists() and not overwrite:
        return True
    if suffix is not None and number is not None:
        archive_path = _find_archive(local_source, suffix)
        if archive_path is not None:
            with zipfile.ZipFile(archive_path) as archive:
                entry = _archive_card_entries(archive).get(number)
                if entry is not None:
                    _atomic_write(destination, archive.read(entry))
                    return True

    key = _collector_key(collector_number)
    if key is None:
        return False
    payload = _cached_set_art(str(local_source.resolve()), set_code).get(key)
    if payload is None:
        return False
    _atomic_write(destination, payload)
    return True


def import_radiant_collections(source: Path) -> dict[str, int]:
    """Install native RC artwork and the original per-card masks, if present.

    No masks are synthesized: cards without a native per-card mask retain
    their existing material metadata/shared client shader.
    """
    from spirit.tools.import_foil_masks import extract_set

    totals = {"written": 0, "unchanged": 0, "unavailable": 0,
              "masks_written": 0, "masks_unchanged": 0}
    # Mask import overlays oldest to newest (art lookup prefers SM first).
    caches = [str(path) for path in reversed(_cache_archives(source))]
    for scripts in sorted(CARD_SCRIPT_DIR.iterdir()):
        layout = RADIANT_COLLECTIONS.get(scripts.name.upper())
        if not scripts.is_dir() or layout is None:
            continue
        offset, count = layout
        for script in sorted(scripts.glob("*.py")):
            number = _collector_from_script(scripts.name.upper(), script.stem)
            if number is None or not offset < number <= offset + count:
                continue
            destination = CARD_ASSET_DIR / scripts.name / f"{script.stem}.png"
            previous = destination.read_bytes() if destination.is_file() else None
            if not install_card_art(scripts.name, number, destination, source):
                totals["unavailable"] += 1
            elif previous == destination.read_bytes():
                totals["unchanged"] += 1
            else:
                totals["written"] += 1
        if caches:
            written, unchanged = extract_set(
                scripts.name, caches, force=True,
                only_cards=list(range(offset + 1, offset + count + 1)),
            )
            totals["masks_written"] += written
            totals["masks_unchanged"] += unchanged
    return totals


def import_premium_xy_foils(source: Path) -> dict:
    """Refresh exact Premium XY prints, never their regular-print masks."""
    from spirit.game.foil_variants import PREMIUM_XY_FOIL_VARIANTS
    from spirit.tools import import_foil_masks as masks

    directories = {path.name.upper(): path.name for path in CARD_SCRIPT_DIR.iterdir()
                   if path.is_dir()}
    sets = [(directories.get(code, code), variants)
            for code, variants in PREMIUM_XY_FOIL_VARIANTS.items()]
    caches = [str(path) for path in reversed(_cache_archives(source))]
    # Also support an extracted cache, with its revisions applied last.
    if any(masks._bundle_payloads(str(source), code, 'std')
           for code, variants in sets):
        caches.append(str(source))
    if not caches:
        return {'written': 0, 'missing': [], 'available': False}
    written, missing = 0, []
    for code, variants in sets:
        count, _ = masks.extract_set(code, caches, force=True,
                                     only_cards=list(variants))
        written += count
        stems = masks._set_card_stems(code)
        for slot in variants:
            stem = stems.get(slot.zfill(3))
            if not stem or not (CARD_ASSET_DIR / code / f'{stem}_foil.png').is_file():
                missing.append(f'{code}/{slot}')
    return {'written': written, 'missing': missing, 'available': True}


def import_swsh_promo_foils(source: Path) -> dict:
    """Import exact original promo masks; never infer missing print finishes."""
    from spirit.tools import import_foil_masks as masks
    sources = [str(path) for path in reversed(_cache_archives(source))]
    for directory in (source, source / 'bundleCache'):
        if any(masks._bundle_payloads(str(directory), 'Promo_SWSH', kind)
               for kind in masks.KIND_SUFFIXES):
            sources.append(str(directory))
    if not sources:
        print('[swsh-promos] No native cache found; foil masks were not installed.')
        return {'written': 0, 'unchanged': 0, 'available': False}
    written, unchanged = masks.extract_set('Promo_SWSH', sources, force=True, strict=True)
    print(f'[swsh-promos] {written} exact masks installed; {unchanged} unchanged. '
          'Printings absent from these bundles do not receive a substitute mask.')
    return {'written': written, 'unchanged': unchanged, 'available': bool(written or unchanged)}


def import_card_art(source: Path) -> dict[str, int]:
    """Replace implemented card PNGs with matching native PTCGO textures."""
    totals = {"sets": 0, "written": 0, "unchanged": 0, "unavailable": 0}
    archive_sets: set[str] = set()
    for set_code, suffix in CARD_ARCHIVES.items():
        scripts = CARD_SCRIPT_DIR / set_code
        if not scripts.is_dir():
            continue
        archive_path = _find_archive(source, suffix)
        if archive_path is None:
            continue
        archive_sets.add(set_code)
        set_written = 0
        with zipfile.ZipFile(archive_path) as archive:
            entries = _archive_card_entries(archive)
            for script in sorted(scripts.glob("*.py")):
                number = _collector_from_script(set_code, script.stem)
                if excluded_print(set_code, number):
                    continue
                entry = entries.get(number) if number is not None else None
                if entry is None:
                    totals["unavailable"] += 1
                    continue
                destination = CARD_ASSET_DIR / set_code / f"{script.stem}.png"
                payload = archive.read(entry)
                if destination.is_file() and destination.read_bytes() == payload:
                    totals["unchanged"] += 1
                    continue
                _atomic_write(destination, payload)
                totals["written"] += 1
                set_written += 1
        totals["sets"] += 1
        print(f"[cards] {set_code}: {set_written} texture(s) updated")

    # Fill collections without a ready image archive directly from their
    # original Unity cache bundles.  Ready PNG archives stay preferred because
    # they avoid a decode/re-encode round trip.
    for scripts in sorted(path for path in CARD_SCRIPT_DIR.iterdir() if path.is_dir()):
        set_code = scripts.name
        if set_code.upper() in archive_sets:
            continue
        cached = _cached_set_art(str(source.resolve()), set_code)
        if not cached:
            continue
        set_written = 0
        for script in sorted(scripts.glob("*.py")):
            key = _collector_key_from_script(set_code, script.stem)
            if excluded_print(set_code, key):
                continue
            payload = cached.get(key) if key is not None else None
            if payload is None:
                totals["unavailable"] += 1
                continue
            destination = CARD_ASSET_DIR / set_code / f"{script.stem}.png"
            if destination.is_file() and destination.read_bytes() == payload:
                totals["unchanged"] += 1
                continue
            _atomic_write(destination, payload)
            totals["written"] += 1
            set_written += 1
        totals["sets"] += 1
        print(f"[cards/cache] {set_code}: {set_written} texture(s) updated")
    return totals


def _cache_bundle_name(path: str) -> str | None:
    normalized = path.replace("\\", "/")
    marker = "/bundleCache/"
    if marker not in normalized:
        return None
    remainder = normalized.split(marker, 1)[1]
    return remainder.split("/", 1)[0] or None


def _is_original_ui_bundle(bundle_name: str) -> bool:
    """Select original visual bundles used by menus and the collection.

    Collection products are deliberately included here.  Their pictures live
    in the same downloaded Unity cache as cards, but are not card-set bundles:
    omitting them leaves packs, sleeves, coins, deck boxes and avatars without
    their original artwork even when the local cache contains it.
    """
    lowered = bundle_name.casefold()
    return lowered.startswith(
        (
            "en_us_landingpage_",
            "en_us_background_",
            "en_us_logos_",
            "en_us_registrationimages_",
            "en_us_seticons_",
            "en_us_shopbanners_",
            "en_us_avatar_",
            "en_us_avatar_thumbs_",
            "en_us_cardsleeves_",
            "en_us_coins_",
            "en_us_deckboxes_",
            "en_us_deckboxflats_",
            "en_us_packs_",
            "en_us_pcdboxes_",
            "en_us_newitemstar_",
            "en_us_traineropponentdeck_",
            "en_us_trainerplayerdeck_",
            "en_us_newalideck_",
            "en_us_newcalvindeck_",
            "en_us_newelladeck_",
            "en_us_newotisdeck_",
            "en_us_newplayerdeck_",
            "en_us_newzachdeck_",
        )
    )


def import_ui_bundles(source: Path) -> dict[str, int]:
    """Restore the original visual menu bundles from the newest local cache."""
    cache_path = source / "SM Cache.zip"
    if not cache_path.is_file():
        cache_path = source / "BW Cache.zip"
    if not cache_path.is_file():
        raise FileNotFoundError("SM Cache.zip or BW Cache.zip was not found")

    totals = {"bundles": 0, "files": 0, "written": 0, "unchanged": 0}
    seen_bundles: set[str] = set()
    with zipfile.ZipFile(cache_path) as archive:
        for info in archive.infolist():
            normalized = info.filename.replace("\\", "/")
            bundle_name = _cache_bundle_name(normalized)
            if bundle_name is None or not _is_original_ui_bundle(bundle_name):
                continue
            relative = normalized.split(f"/bundleCache/{bundle_name}/", 1)[-1]
            if relative not in {
                "00000000000000000000000001000000/__data",
                "00000000000000000000000001000000/__info",
            }:
                continue
            payload = archive.read(info)
            destination = EXTERNAL_CACHE_DIR / bundle_name / relative
            totals["files"] += 1
            seen_bundles.add(bundle_name)
            if destination.is_file() and destination.read_bytes() == payload:
                totals["unchanged"] += 1
                continue
            _atomic_write(destination, payload)
            totals["written"] += 1
    totals["bundles"] = len(seen_bundles)
    return totals


def seed_original_landing_pages(force: bool = False) -> int:
    """Restore a native SWSH10 home carousel when no landing page exists."""
    from spirit.database.economy_data import (
        delete_dynamic_page,
        list_dynamic_pages,
        upsert_dynamic_page,
    )
    from spirit.server.dynamic_pages import FOREVER_MS, normalize_page

    current = list_dynamic_pages(page_type="landing")
    if current and not force:
        print("[menus] Existing landing pages kept unchanged")
        return 0
    if force:
        for page in current:
            delete_dynamic_page(page["id"])

    created = 0
    for order, (asset_name, title) in enumerate(
        zip(_LANDING_PAGE_NAMES, _LANDING_PAGE_TITLES)
    ):
        request_path = f"LandingPage/{asset_name}"
        content = normalize_page(
            {
                "template": "LandingPageLeftNoButtons",
                "startTime": 0,
                "endTime": FOREVER_MS,
                "labels": {
                    "GameText": {
                        "token": "",
                        "bundle": {"en_US": title, "pt_BR": title},
                    }
                },
                "images": {
                    "GameBackground": {
                        "localeImageMap": {
                            "en_US": request_path,
                            "pt_BR": request_path,
                        }
                    }
                },
                "actions": {},
            },
            "landing",
            order,
        )
        upsert_dynamic_page(
            content, page_type="landing", sort_order=order, enabled=True
        )
        created += 1
    return created


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Import native card and menu artwork from a local PTCGO folder."
    )
    parser.add_argument(
        "--source",
        default=os.environ.get(SOURCE_ENV, str(DEFAULT_SOURCE_DIR)),
        help=f"PTCGO asset directory (default: %(default)s; env: {SOURCE_ENV})",
    )
    parser.add_argument("--cards-only", action="store_true")
    parser.add_argument("--ui-only", action="store_true")
    parser.add_argument("--radiant-only", action="store_true",
                        help="Import only native Radiant Collection artwork and masks")
    parser.add_argument("--premium-xy-only", action="store_true",
                        help="Refresh only the 14 exact Premium Trainer's XY foil masks")
    parser.add_argument("--vunion-only", action="store_true",
                        help="Install the 20 V-UNION parts, five complete faces and original foil masks")
    parser.add_argument(
        "--replace-landing-pages",
        action="store_true",
        help="Replace existing landing-page configuration with the local carousel.",
    )
    args = parser.parse_args()

    source = source_directory(args.source)
    if not source.is_dir():
        parser.error(f"PTCGO asset directory does not exist: {source}")
    if args.cards_only and args.ui_only:
        parser.error("--cards-only and --ui-only cannot be combined")
    if args.radiant_only and args.ui_only:
        parser.error("--radiant-only and --ui-only cannot be combined")
    if args.premium_xy_only and (args.ui_only or args.radiant_only):
        parser.error("--premium-xy-only cannot be combined with --ui-only or --radiant-only")
    if args.vunion_only and (args.ui_only or args.radiant_only or args.premium_xy_only):
        parser.error("--vunion-only cannot be combined with another targeted or UI import")
    if args.vunion_only:
        from spirit.tools.import_vunion import import_vunion
        return 2 if import_vunion(source) else 0

    premium_failed = False
    if not args.ui_only and not args.radiant_only:
        premium = import_premium_xy_foils(source)
        if not premium['available']:
            print('[premium-xy] No native cache found; exact foil masks were not installed.')
        else:
            print(f"[premium-xy] {premium['written']} masks installed; "
                  f"{len(premium['missing'])} exact prints unavailable.")
            for card in premium['missing']:
                print(f'[premium-xy] Missing exact mask: {card}')
        premium_failed = bool(premium['missing'])
        if args.premium_xy_only:
            return 2 if premium_failed or not premium['available'] else 0

    if not args.ui_only:
        radiant = import_radiant_collections(source)
        print(f"[radiant] {radiant['written']} artwork updated, "
              f"{radiant['unchanged']} unchanged, "
              f"{radiant['masks_written']} native masks imported, "
              f"{radiant['unavailable']} artwork without a local match")
        if args.radiant_only:
            return 2 if radiant['unavailable'] else 0

    energy_failures = []
    vunion_failures = []
    if not args.ui_only:
        card_totals = import_card_art(source)
        import_swsh_promo_foils(source)
        # Composite V-UNION faces have nonnumeric native texture names, so
        # they need the dedicated importer in addition to physical card art.
        from spirit.tools.import_vunion import import_vunion
        vunion_failures = import_vunion(source)
        print(
            "[cards] done: "
            f"{card_totals['written']} updated, "
            f"{card_totals['unchanged']} already native, "
            f"{card_totals['unavailable']} without a local match"
        )
        # The generic cache scan skips sets with no matches. Basic Energy is
        # required, so explicitly install/verify every print before reporting
        # success, using the same source selected for this installation.
        from spirit.tools.install_recent_card_art import install_native_energy

        energy_failures = install_native_energy(False, str(source))
        for failure in energy_failures:
            print("[cards] " + failure)
    if not args.cards_only:
        ui_totals = import_ui_bundles(source)
        print(
            "[menus] done: "
            f"{ui_totals['bundles']} bundles, "
            f"{ui_totals['written']} files updated, "
            f"{ui_totals['unchanged']} unchanged"
        )
        created = seed_original_landing_pages(args.replace_landing_pages)
        print(f"[menus] {created} original home landing page(s) created")
    return 2 if energy_failures or premium_failed or vunion_failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
