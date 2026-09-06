"""Extract original PTCGO foil-mask textures into per-card _foil PNGs.

Reads the wp_{kind}_Foil2 bundles from the original game cache and saves each
mask whose collector number matches a card script as
assets/cards/{SET}/{Script}_foil[{kind}].png, where auto_bundle picks them up
and rebuilds the en_US_{SET}_wp_{kind}_Foil2 bundles the client requests.

Usage:
    python -m spirit.tools.import_foil_masks --set SWSH4
    python -m spirit.tools.import_foil_masks --all [--force]
"""
import argparse
import glob
import os
import re
import sys

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
    return stems


def _bundle_data_paths(cache_dir: str, set_code: str, kind: str) -> list:
    """__data paths for every cached version of one foil bundle, oldest first
    (newer versions carry later promo additions and win on texture collisions)."""
    pattern = os.path.join(cache_dir, f"en_US_{set_code}_wp_{kind}_Foil2_*")
    paths = []
    for d in glob.glob(pattern):
        for root, _, files in os.walk(d):
            if "__data" in files:
                paths.append(os.path.join(root, "__data"))
                break
    paths.sort(key=os.path.getmtime)
    return paths


def extract_set(set_code: str, cache_dir: str, force: bool = False, only_cards=None) -> tuple:
    import UnityPy

    stems = _set_card_stems(set_code)
    if only_cards:
        wanted = {str(c).zfill(3) for c in only_cards}
        stems = {num: stem for num, stem in stems.items() if num in wanted}
    if not stems:
        print(f"[{set_code}] no matching card scripts found, skipping")
        return (0, 0)

    written = skipped = 0
    for kind, suffix in KIND_SUFFIXES.items():
        textures = {}
        for data_path in _bundle_data_paths(cache_dir, set_code, kind):
            try:
                env = UnityPy.load(data_path)
                for obj in env.objects:
                    if obj.type.name != "Texture2D":
                        continue
                    data = obj.read()
                    textures[data.m_Name] = data
            except Exception as e:
                print(f"[{set_code}] failed to load {data_path}: {e}")

        for tex_name, data in sorted(textures.items()):
            stem = stems.get(tex_name.zfill(3))
            if not stem:
                continue
            out_path = os.path.join(CARDS_IMG_DIR, set_code, f"{stem}{suffix}.png")
            if os.path.exists(out_path) and not force:
                skipped += 1
                continue
            os.makedirs(os.path.dirname(out_path), exist_ok=True)
            try:
                data.image.save(out_path)
                written += 1
            except Exception as e:
                print(f"[{set_code}] failed to save {out_path}: {e}")
        if textures:
            matched = sum(1 for t in textures if t.zfill(3) in stems)
            print(f"[{set_code}] wp_{kind}: {len(textures)} masks in cache, {matched} match card scripts")

    print(f"[{set_code}] wrote {written} mask PNGs ({skipped} already present)")
    return (written, skipped)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--set", dest="set_code", help="Set code, e.g. SWSH4")
    parser.add_argument("--all", action="store_true", help="Extract every set with card scripts")
    parser.add_argument("--cache-dir", default=DEFAULT_CACHE_DIR)
    parser.add_argument("--force", action="store_true", help="Overwrite existing _foil PNGs")
    parser.add_argument("--card", action="append", dest="cards",
                        help="Only these collector numbers (repeatable)")
    args = parser.parse_args()

    if not os.path.isdir(args.cache_dir):
        print(f"Cache dir not found: {args.cache_dir}")
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
        w, _ = extract_set(set_code, args.cache_dir, force=args.force, only_cards=args.cards)
        total_written += w
    print(f"Done. {total_written} masks written.")


if __name__ == "__main__":
    main()
