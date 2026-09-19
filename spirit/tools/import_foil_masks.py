"""Extract original PTCGO foil-mask textures into per-card _foil PNGs.

Reads the wp_{kind}_Foil2 bundles from the original game cache and saves each
mask whose collector number matches a card script as
assets/cards/{SET}/{Script}_foil[{kind}].png, where auto_bundle picks them up
and rebuilds the en_US_{SET}_wp_{kind}_Foil2 bundles the client requests.

Usage:
    python -m spirit.tools.import_foil_masks --set SWSH4
    python -m spirit.tools.import_foil_masks --all [--force]
    python -m spirit.tools.import_foil_masks --all \
        --cache "BW Cache.zip" --cache "SM Cache.zip" --force

Cache sources may be an extracted ``bundleCache`` directory or a complete
PTCGO cache ZIP.  Sources are applied from left to right; when two archives
contain the same mask, the source listed last wins.
"""
import argparse
import json
import os
import re
import shutil
import sys
import zipfile
from dataclasses import dataclass
from datetime import datetime
from typing import Optional, Union

from spirit.game.foil_variants import PREMIUM_XY_FOIL_VARIANTS
from spirit.game.excluded_prints import excluded_print

DEFAULT_CACHE_DIR = os.path.join(
    "original_game_cache",
    "The Pokemon Company International",
    "Pokemon Trading Card Game Online",
    "bundleCache",
)
SCRIPTS_DIR = os.path.join("spirit", "game", "scripts", "cards")
CARDS_IMG_DIR = os.path.join("spirit", "assets", "cards")

# wp bundle kind -> filename suffix (mirrors auto_bundle.FOIL_KIND_SUFFIXES)
KIND_SUFFIXES = {
    "std": "_foil",
    "ph": "_foil_ph",
    "pcd": "_foil_pcd",
    "secondary": "_foil_secondary",
}

_COLLECTOR_RE = re.compile(r"collector_number\s*=\s*(\d+)")

# Repository set codes which differ from the original PTCGO bundle names.
# Exact repository codes are checked last so they win if a cache contains both.
CACHE_SET_ALIASES = {
    "BWP": ("PROMO_BW",),
    "CEL25": ("Ann25th",),
    "CEL25C": ("Ann25thR",),
    "SMP": ("Promo_SM",),
    "SM35": ("SL",),
    "SM75": ("DM",),
    "DET1": ("GUM",),
    "SM115": ("HF",),
    "SWSH35": ("CP",),
    "SWSH45": ("SF",),
    "SWSHP": ("Promo_SWSH",),
    "XYP": ("Promo_XY",),
}

INTERNAL_FOIL_ALIASES = {
    "XY3": {"114": "55"},
    "XY4": {"125": "24"},
    "XY6": {"114": "92"},
    "XY8": {"166": "146"},
    "XY9": {"127": "98", "129": "107"},
    "TWENTIETHANN": {"133": "28"},
    "XY10": {"131": "54"},
}


@dataclass(frozen=True)
class BundlePayload:
    """One serialized Unity bundle from either disk or a ZIP archive."""

    label: str
    modified: tuple
    path: Optional[str] = None
    archive: Optional[str] = None
    member: Optional[str] = None

    def load_arg(self) -> Union[str, bytes]:
        if self.path is not None:
            return self.path
        with zipfile.ZipFile(self.archive) as cache_zip:
            return cache_zip.read(self.member)


def _set_card_stems(set_code: str) -> dict:
    """{padded collector number: script stem} for one set's card scripts."""
    stems = {}
    set_dir = os.path.join(SCRIPTS_DIR, set_code)
    if not os.path.isdir(set_dir):
        return stems
    for name in os.listdir(set_dir):
        if not name.endswith(".py") or name == "__init__.py":
            continue
        stem = name[:-3]
        try:
            with open(os.path.join(set_dir, name), encoding="utf-8") as f:
                m = _COLLECTOR_RE.search(f.read())
        except OSError:
            continue
        if m:
            stems[m.group(1).zfill(3)] = stem
        else:
            tail = re.search(r"_(\d+)$", stem)
            if tail:
                stems[tail.group(1).zfill(3)] = stem
    return {number: stem for number, stem in stems.items()
            if not excluded_print(set_code, number)}


def _bundle_name_pattern(set_code: str, kind: str) -> re.Pattern:
    prefix = re.escape(f"en_US_{set_code}_wp_{kind}_Foil2")
    return re.compile(
        rf"(?:^|/){prefix}(?:_[^/]*)?/[0-9a-fA-F]{{32}}/__data$",
        re.IGNORECASE,
    )


def _bundle_revision(name: str) -> tuple[int, int]:
    """Return the semantic cache revision encoded in a bundle name.

    ZIP timestamps are not reliable indicators of PTCGO bundle order (some
    archives contain CR105 entries dated before CR100).  Sorting by those
    timestamps made an older mask overwrite a corrected newer one.
    """
    match = re.search(r"_CRR?(\d+)(?:_(\d+))?(?:/|$)", name, re.IGNORECASE)
    if not match:
        return (0, 0)
    return (int(match.group(1)), int(match.group(2) or 0))


def _directory_payloads(cache_dir: str, set_code: str, kind: str) -> list:
    """Serialized bundle paths from one extracted cache, oldest first."""
    prefix = f"en_US_{set_code}_wp_{kind}_Foil2"
    payloads = []
    if not os.path.isdir(cache_dir):
        return payloads
    for name in os.listdir(cache_dir):
        if not (name == prefix or name.startswith(prefix + "_")):
            continue
        bundle_dir = os.path.join(cache_dir, name)
        for root, _, files in os.walk(bundle_dir):
            if "__data" not in files:
                continue
            path = os.path.join(root, "__data")
            payloads.append(BundlePayload(
                label=path,
                modified=(*_bundle_revision(name), os.path.getmtime(path), path),
                path=path,
            ))
            break
    return sorted(payloads, key=lambda item: item.modified)


def _zip_payloads(cache_zip: str, set_code: str, kind: str) -> list:
    """Serialized bundle members from one cache ZIP, oldest first."""
    pattern = _bundle_name_pattern(set_code, kind)
    payloads = []
    with zipfile.ZipFile(cache_zip) as archive:
        for info in archive.infolist():
            member = info.filename.replace("\\", "/")
            if not pattern.search(member):
                continue
            payloads.append(BundlePayload(
                label=f"{cache_zip}!{info.filename}",
                modified=(
                    *_bundle_revision(member),
                    datetime(*info.date_time).timestamp(),
                    info.header_offset,
                ),
                archive=cache_zip,
                member=info.filename,
            ))
    return sorted(payloads, key=lambda item: item.modified)


def _bundle_payloads(cache_source: str, set_code: str, kind: str) -> list:
    """Return every cached version of a foil bundle from one source."""
    if os.path.isfile(cache_source) and zipfile.is_zipfile(cache_source):
        return _zip_payloads(cache_source, set_code, kind)
    return _directory_payloads(cache_source, set_code, kind)


def _cache_set_codes(set_code: str) -> tuple:
    return (*CACHE_SET_ALIASES.get(set_code.upper(), ()), set_code)


def _collector_texture_number(name: str) -> Optional[str]:
    """Normalize an ordinary collector-number mask, excluding print variants."""
    value = str(name).strip()
    if not value.isdigit():
        return None
    return value.zfill(3)


def _variant_aliases(set_code: str) -> dict:
    """Return {native texture name: internal collector slot} for variants.

    PTCGO names alternate Sun & Moon prints ``019xy``, ``130ya``, etc.,
    while the protocol only accepts numeric collector slots.  The era importer
    writes the reversible mapping beside the art so the original variant foil
    mask is selected rather than copying the base print's material.
    """
    path = os.path.join(CARDS_IMG_DIR, set_code, "foil_aliases.json")
    try:
        with open(path, encoding="utf-8") as source:
            aliases = json.load(source)
    except (OSError, ValueError, TypeError):
        aliases = {}
    # Built-in identities also work on clean installs without a generated
    # foil_aliases.json. Exact verified mappings win over older local aliases.
    aliases.update(PREMIUM_XY_FOIL_VARIANTS.get(set_code.upper(), {}))
    return {
        str(native).strip().casefold(): str(internal).zfill(3)
        for internal, native in aliases.items()
    }


def extract_set(set_code: str, cache_sources, force: bool = False, only_cards=None,
                strict: bool = False, container_only: bool = False) -> tuple:
    import UnityPy

    stems = _set_card_stems(set_code)
    if only_cards:
        wanted = {str(c).zfill(3) for c in only_cards}
        stems = {num: stem for num, stem in stems.items() if num in wanted}
    if not stems:
        print(f"[{set_code}] no matching card scripts found, skipping")
        return (0, 0)
    variant_aliases = _variant_aliases(set_code)
    exact_variants = {
        internal.zfill(3): native.casefold()
        for internal, native in PREMIUM_XY_FOIL_VARIANTS.get(set_code.upper(), {}).items()
    }

    written_paths = set()
    skipped_paths = set()
    for kind, suffix in KIND_SUFFIXES.items():
        found = matched = 0
        payload_count = 0
        # Each successive bundle revision and cache source may replace an
        # earlier texture.  Files created during this invocation are therefore
        # intentionally overwritten; pre-existing files require --force.
        for cache_source in cache_sources:
            for cache_set_code in _cache_set_codes(set_code):
                for payload in _bundle_payloads(cache_source, cache_set_code, kind):
                    payload_count += 1
                    try:
                        env = UnityPy.load(payload.load_arg())
                    except Exception as e:
                        if strict:
                            raise ValueError(f"Cannot read {payload.label}: {e}") from e
                        print(f"[{set_code}] failed to load {payload.label}: {e}")
                        continue
                    objects = env.objects
                    if container_only:
                        # Generated bundles retain unused template objects.
                        # Only container references are actually served; raw
                        # object traversal can install another card's mask.
                        objects = list({(obj.file_id, obj.path_id): obj
                                        for obj in env.container.values()}.values())
                    for obj in objects:
                        if obj.type.name != "Texture2D":
                            continue
                        data = obj.read()
                        found += 1
                        number = variant_aliases.get(
                            str(data.m_Name).strip().casefold()
                        ) or _collector_texture_number(data.m_Name)
                        # A native numeric mask can coincide with a server-only
                        # alternate slot (XY9/128). It is not that alternate.
                        if number in exact_variants and str(data.m_Name).strip().casefold() != exact_variants[number]:
                            continue
                        stem = stems.get(number) if number else None
                        if not stem:
                            continue
                        matched += 1
                        out_path = os.path.join(
                            CARDS_IMG_DIR, set_code, f"{stem}{suffix}.png"
                        )
                        if (os.path.exists(out_path)
                                and out_path not in written_paths
                                and not force):
                            skipped_paths.add(out_path)
                            continue
                        os.makedirs(os.path.dirname(out_path), exist_ok=True)
                        try:
                            # Copy detaches the PIL image from UnityPy's serialized
                            # reader before the next large bundle is loaded.
                            data.image.copy().save(out_path)
                            written_paths.add(out_path)
                            skipped_paths.discard(out_path)
                        except Exception as e:
                            if strict:
                                raise ValueError(f"Cannot save {out_path}: {e}") from e
                            print(f"[{set_code}] failed to save {out_path}: {e}")
                    del env
        if strict and payload_count and not matched:
            raise ValueError(f"{set_code}/wp_{kind}: no matching native masks found")
        if found:
            print(
                f"[{set_code}] wp_{kind}: {found} masks inspected, "
                f"{matched} matching textures"
            )

    # A forced refresh of these exact prints must also remove old regular /
    # reverse masks for which the selected archives contain no variant mask.
    # Never fall back to the regular artwork's mask.
    if force:
        asset_root = os.path.realpath(CARDS_IMG_DIR)
        for internal in PREMIUM_XY_FOIL_VARIANTS.get(set_code.upper(), {}):
            stem = stems.get(internal.zfill(3))
            if stem is None:
                continue
            for suffix in KIND_SUFFIXES.values():
                path = os.path.join(CARDS_IMG_DIR, set_code, f"{stem}{suffix}.png")
                resolved = os.path.realpath(path)
                if os.path.commonpath([asset_root, resolved]) != asset_root:
                    raise ValueError(f"Mask path is outside card assets: {path}")
                if path not in written_paths and os.path.isfile(path):
                    os.remove(path)
                    skipped_paths.discard(path)
                    print(f"[{set_code}] removed unmatched alternate-print mask: {stem}{suffix}.png")

    # Physical promo variants can share the original collector number even
    # though the server assigns them a unique internal slot.  Reuse the base
    # cache mask so every imported print receives the original material.
    for destination_number, source_number in INTERNAL_FOIL_ALIASES.get(
        set_code.upper(), {}
    ).items():
        destination_stem = stems.get(destination_number.zfill(3))
        source_stem = stems.get(source_number.zfill(3))
        if not destination_stem or not source_stem:
            continue
        for suffix in KIND_SUFFIXES.values():
            source_path = os.path.join(
                CARDS_IMG_DIR, set_code, f"{source_stem}{suffix}.png"
            )
            destination_path = os.path.join(
                CARDS_IMG_DIR, set_code, f"{destination_stem}{suffix}.png"
            )
            if not os.path.exists(source_path):
                continue
            if os.path.exists(destination_path) and not force:
                skipped_paths.add(destination_path)
                continue
            shutil.copyfile(source_path, destination_path)
            written_paths.add(destination_path)
            skipped_paths.discard(destination_path)

    print(
        f"[{set_code}] wrote {len(written_paths)} mask PNGs "
        f"({len(skipped_paths)} already present)"
    )
    return (len(written_paths), len(skipped_paths))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--set", dest="set_code", help="Set code, e.g. SWSH4")
    parser.add_argument("--all", action="store_true", help="Extract every set with card scripts")
    parser.add_argument(
        "--cache", action="append", dest="cache_sources",
        help=("Extracted bundleCache directory or complete cache ZIP. Repeat "
              "to overlay sources; the last source wins."),
    )
    parser.add_argument(
        "--cache-dir", dest="legacy_cache_dir",
        help="Deprecated alias for one extracted cache directory",
    )
    parser.add_argument("--force", action="store_true", help="Overwrite existing _foil PNGs")
    parser.add_argument("--card", action="append", dest="cards",
                        help="Only these collector numbers (repeatable)")
    args = parser.parse_args()

    cache_sources = args.cache_sources or [args.legacy_cache_dir or DEFAULT_CACHE_DIR]
    missing = [source for source in cache_sources if not os.path.exists(source)]
    if missing:
        for source in missing:
            print(f"Cache source not found: {source}")
        sys.exit(1)

    if args.all:
        set_codes = sorted(
            d for d in os.listdir(SCRIPTS_DIR)
            if os.path.isdir(os.path.join(SCRIPTS_DIR, d)) and not d.startswith("__")
        )
    elif args.set_code:
        set_codes = [args.set_code]
    else:
        parser.error("pass --set <CODE> or --all")

    total_written = 0
    for set_code in set_codes:
        w, _ = extract_set(
            set_code, cache_sources, force=args.force, only_cards=args.cards
        )
        total_written += w
    print(f"Done. {total_written} masks written.")


if __name__ == "__main__":
    main()
