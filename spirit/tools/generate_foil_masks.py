"""Generate (or preview) procedural foil masks for cards.

The auto_bundle startup scan already generates masks for every foil-flagged
card lacking an extracted/hand-authored _foil PNG; this tool exists to force
regeneration after tuning foil_mask_gen.py and to preview a mask composited
on white without launching the client.

Usage:
    python -m spirit.tools.generate_foil_masks --set SWSH2 --card 135 --preview out.png
    python -m spirit.tools.generate_foil_masks --set SWSH2 --force
"""
import argparse
import importlib.util
import os
import sys

from PIL import Image

from spirit.server import foil_mask_gen
from spirit.server.auto_bundle import (
    CARDS_IMG_DIR, FOIL_GEN_DIR, FOIL_SUFFIX_BY_KIND,
)

SCRIPTS_DIR = os.path.join("spirit", "game", "scripts", "cards")


def _load_defs(set_code, only_cards=None):
    wanted = {str(c).zfill(3) for c in (only_cards or [])}
    set_dir = os.path.join(SCRIPTS_DIR, set_code)
    defs = []
    for name in sorted(os.listdir(set_dir)):
        if not name.endswith(".py") or name == "__init__.py":
            continue
        path = os.path.join(set_dir, name)
        spec = importlib.util.spec_from_file_location(f"foilgen_{set_code}_{name[:-3]}", path)
        module = importlib.util.module_from_spec(spec)
        try:
            spec.loader.exec_module(module)
        except Exception as e:
            print(f"skip {name}: {e}")
            continue
        card_def = getattr(module, "card", None)
        if card_def is None or getattr(card_def, "foil", None) is None:
            continue
        num = str(card_def.collector_number).zfill(3)
        if wanted and num not in wanted:
            continue
        defs.append((num, name[:-3], card_def))
    return defs


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--set", dest="set_code", required=True)
    parser.add_argument("--card", action="append", dest="cards",
                        help="Only these collector numbers (repeatable)")
    parser.add_argument("--style", choices=("auto",) + foil_mask_gen.STYLES, default="auto")
    parser.add_argument("--preview", help="Write a white-composited preview PNG here instead of the cache")
    parser.add_argument("--force", action="store_true", help="Regenerate even if up to date")
    args = parser.parse_args()

    defs = _load_defs(args.set_code, args.cards)
    if not defs:
        print("No foil-flagged card scripts matched.")
        sys.exit(1)

    for num, stem, card_def in defs:
        art = os.path.join(CARDS_IMG_DIR, args.set_code, f"{stem}.png")
        if not os.path.exists(art):
            print(f"[{args.set_code}/{num}] no art PNG, skipping")
            continue
        foil = card_def.foil
        style = args.style if args.style != "auto" else foil.resolve_style(
            getattr(card_def, "rarity", None), getattr(card_def, "subtypes", None))
        if args.preview:
            mask = foil_mask_gen.generate_mask(art, style)
            bg = Image.new("RGBA", mask.size, (255, 255, 255, 255))
            bg.alpha_composite(mask)
            bg.convert("RGB").save(args.preview)
            print(f"[{args.set_code}/{num}] preview ({style}) -> {args.preview}")
            continue
        out = os.path.join(FOIL_GEN_DIR, args.set_code,
                           f"{num}{FOIL_SUFFIX_BY_KIND[foil.mask_kind()]}.png")
        if args.force and os.path.exists(out):
            os.remove(out)
        if foil_mask_gen.generate_mask_png(art, out, style):
            print(f"[{args.set_code}/{num}] generated ({style}) -> {out}")


if __name__ == "__main__":
    main()
