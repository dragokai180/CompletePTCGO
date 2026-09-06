import os
import sys
import logging
import subprocess
import json
import importlib.util
import math
from PIL import Image, ImageFilter

from spirit.game.attributes import AttrID, TrainerType
from spirit.game.scripts.cards import loader
from spirit.server.auto_bundle_cosmetics import compile_all_cosmetics
from spirit.server import dynamic_pages
from spirit.server import foil_mask_gen

ASSETS_DIR = "spirit/assets"
BUNDLE_CACHE_DIR = os.path.join(ASSETS_DIR, "bundleCache")
PIP_CACHE_DIR = os.path.join(BUNDLE_CACHE_DIR, "pips")
CARDS_IMG_DIR = os.path.join(ASSETS_DIR, "cards")
CREATE_BUNDLE_SCRIPT = "re_tools/create_card_bundle.py"
# The default template used by create_card_bundle.py
DEFAULT_TEMPLATE = "spirit/templates/card_bundle"

def _generate_bundle(bundle_name, mapping, keep_size=False) -> int:
    bundle_path = os.path.join(BUNDLE_CACHE_DIR, bundle_name, "00000000000000000000000001000000", "__data")

    # Rebuild check
    map_path = "spirit/server/asset_map.json"
    rebuild_needed = not os.path.exists(bundle_path)

    if not rebuild_needed and os.path.exists(map_path):
        try:
            with open(map_path, "r") as f:
                amap = json.load(f)
            existing_assets = amap.get(bundle_name, [])
            for asset in mapping.keys():
                if asset not in existing_assets:
                    rebuild_needed = True
                    break
        except Exception:
            rebuild_needed = True

    # Rebuild when any source image is newer than the built bundle
    # (replaced card art, regenerated energy pips, new foil masks).
    if not rebuild_needed:
        bundle_mtime = os.path.getmtime(bundle_path)
        for src in mapping.values():
            if os.path.exists(src) and os.path.getmtime(src) > bundle_mtime:
                rebuild_needed = True
                break

    if rebuild_needed:
        logging.info(f"[AutoBundle] Generating bundle '{bundle_name}' ({len(mapping)} assets)...")
        temp_mapping_path = os.path.join(BUNDLE_CACHE_DIR, f"temp_{bundle_name}.json")
        with open(temp_mapping_path, "w") as f:
            json.dump(mapping, f)

        try:
            cmd = [
                sys.executable,
                CREATE_BUNDLE_SCRIPT,
                "--bundle", bundle_name,
                "--mapping", temp_mapping_path,
                "--template", DEFAULT_TEMPLATE
            ]
            if keep_size:
                cmd.append("--keep-size")
            result = subprocess.run(cmd, capture_output=True, text=True)
            if result.returncode != 0:
                logging.error(f"[AutoBundle] Bundle build failed for {bundle_name}: {result.stderr[-500:]}")
            return 1
        finally:
            if os.path.exists(temp_mapping_path):
                os.remove(temp_mapping_path)
    return 0


def self_generate_set_bundle(set_code, set_mapping) -> int:
    return _generate_bundle(f"en_US_{set_code}", set_mapping)


# Foil-mask PNG suffix next to the card art -> the wp_ bundle kind the client
# requests it from ({SET}_wp_{kind}_Foil2/{num}; Reverse masks ride ph,
# Cracked_Ice pcd, second foil effects secondary).
FOIL_KIND_SUFFIXES = {
    "_foil": "std",
    "_foil_ph": "ph",
    "_foil_pcd": "pcd",
    "_foil_secondary": "secondary",
}
FOIL_SUFFIX_BY_KIND = {v: k for k, v in FOIL_KIND_SUFFIXES.items()}
FOIL_GEN_DIR = os.path.join(BUNDLE_CACHE_DIR, "foil_masks")


def ensure_generated_mask(art_png, set_code, asset_name, kind, style):
    """Path to a generated mask PNG, regenerating when the art or the
    generator changed; None on failure."""
    out_path = os.path.join(FOIL_GEN_DIR, set_code,
                            f"{asset_name}{FOIL_SUFFIX_BY_KIND[kind]}.png")
    if os.path.exists(out_path):
        m = os.path.getmtime(out_path)
        if (m >= os.path.getmtime(art_png)
                and m >= os.path.getmtime(foil_mask_gen.__file__)):
            return out_path
    logging.info(f"[AutoBundle] Generating foil mask {set_code}/{asset_name} ({kind}, {style})")
    return out_path if foil_mask_gen.generate_mask_png(art_png, out_path, style) else None


def generate_foil_bundles(foil_sets) -> int:
    """foil_sets: {set_code: {kind: {padded_num: png_path}}} -> built count."""
    count = 0
    for set_code, kinds in foil_sets.items():
        for kind, mapping in kinds.items():
            if mapping:
                count += _generate_bundle(
                    f"en_US_{set_code}_wp_{kind}_Foil2", mapping, keep_size=True
                )
    return count

def _is_special_energy(card_def) -> bool:
    spec = (getattr(card_def, "extra_attributes", None) or {}).get(
        str(AttrID.IS_SPECIAL_ENERGY.value)
    )
    return bool(spec and spec.get("value"))


def _is_pokemon_tool(card_def) -> bool:
    kind = (getattr(card_def, "extra_attributes", None) or {}).get(
        str(AttrID.TRAINER_TYPE.value)
    )
    return bool(kind) and kind.get("value") in (
        TrainerType.POKEMON_TOOL.value, TrainerType.POKEMON_TOOL_F.value
    )


def _detect_emblem_circle(img):
    """(cx, cy, r) of the special energy's strongest circular emblem, or None."""
    found = _detect_emblem_circles(img, limit=1)
    return found[0] if found else None


def _detect_emblem_circles(img, limit=1):
    """Up to `limit` circular emblems, strongest first, as (cx, cy, r).

    Hough-gradient vote on the art window: edge pixels vote along their
    gradient for circle centers; only centers near the art middle compete,
    and a radius bonus prefers the full ball over sharp inner details.

    limit > 1 is for the energies that print one emblem per unit they
    provide (Double Colorless): the pip has to show the pair, or on the
    board it reads as an ordinary one-unit Energy.
    """

    w, h = img.size
    # Art window of an energy card: skip border, title bar and text box.
    rx0, ry0 = int(w * 0.08), int(h * 0.13)
    rx1, ry1 = int(w * 0.92), int(h * 0.66)
    region = img.crop((rx0, ry0, rx1, ry1)).convert("L")

    ds = 150
    scale = ds / region.width
    resample = getattr(Image, "LANCZOS", getattr(Image, "ANTIALIAS", 1))
    small = region.resize((ds, max(3, int(region.height * scale))),
                          resample).filter(ImageFilter.GaussianBlur(1))
    sw, sh = small.size
    px = list(small.getdata())

    def p(x, y):
        return px[y * sw + x]

    edges = []
    for y in range(1, sh - 1):
        for x in range(1, sw - 1):
            gx = (p(x+1, y-1) + 2*p(x+1, y) + p(x+1, y+1)
                  - p(x-1, y-1) - 2*p(x-1, y) - p(x-1, y+1))
            gy = (p(x-1, y+1) + 2*p(x, y+1) + p(x+1, y+1)
                  - p(x-1, y-1) - 2*p(x, y-1) - p(x+1, y-1))
            mag = gx*gx + gy*gy
            if mag > 0:
                edges.append((x, y, gx, gy, mag))
    edges.sort(key=lambda e: -e[4])
    edges = edges[:max(1, len(edges) // 4)]

    # A card that prints one emblem per unit draws the extras smaller and
    # further out (Team Rocket's Energy puts its second ball at 0.78w), so
    # looking for a pair means a smaller floor on the radius and a wider
    # window for the center. Single-emblem detection keeps the tight gates,
    # which are what stop it locking onto an inner highlight.
    pair = limit > 1
    rmin = max(6, int(min(sw, sh) * (0.10 if pair else 0.16)))
    rmax = int(min(sw, sh) * 0.60)
    acc = {}
    for x, y, gx, gy, mag in edges:
        norm = math.sqrt(gx*gx + gy*gy)
        ux, uy = gx / norm, gy / norm
        for r in range(rmin, rmax + 1, 2):
            for sgn in (1, -1):
                cx = int(round(x + sgn * ux * r))
                cy = int(round(y + sgn * uy * r))
                if 0 <= cx < sw and 0 <= cy < sh:
                    acc.setdefault((cx, cy), {})
                    acc[(cx, cy)][r] = acc[(cx, cy)].get(r, 0) + 1

    cx_lo, cx_hi = (sw * 0.12, sw * 0.88) if pair else (sw * 0.25, sw * 0.75)
    cy_lo, cy_hi = (sh * 0.10, sh * 0.90) if pair else (sh * 0.15, sh * 0.85)
    min_votes = len(edges) * 0.02
    ranked = []
    for (cx, cy) in list(acc.keys()):
        if not (cx_lo <= cx <= cx_hi and cy_lo <= cy <= cy_hi):
            continue
        pooled = {}
        for dx in (-1, 0, 1):
            for dy in (-1, 0, 1):
                for r, v in acc.get((cx+dx, cy+dy), {}).items():
                    pooled[r] = pooled.get(r, 0) + v
        best_here, best_here_weighted = None, -1
        for r in pooled:
            score = pooled.get(r-2, 0) + pooled[r] + pooled.get(r+2, 0)
            weighted = score * (1 + 1.5 * r / rmax)
            if weighted > best_here_weighted and score >= min_votes:
                best_here, best_here_weighted = (cx, cy, r), weighted
        if best_here is not None:
            ranked.append((best_here_weighted, best_here))

    if not ranked:
        return []
    # Strongest first, then non-maximum suppression so a second emblem is a
    # genuinely different circle and not the same one re-detected a pixel over.
    ranked.sort(key=lambda t: -t[0])
    inv = 1 / scale
    picked = []
    for _, (cx, cy, r) in ranked:
        if any((cx - ox) ** 2 + (cy - oy) ** 2 < (0.75 * max(r, orr)) ** 2
               for ox, oy, orr in picked):
            continue
        picked.append((cx, cy, r))
        if len(picked) >= limit:
            break
    return [(rx0 + cx * inv, ry0 + cy * inv, r * inv) for cx, cy, r in picked]


def _energy_units(card_def) -> int:
    """How much Energy one copy provides at once, off ENERGY_INFO (Double
    Colorless: 2). Drives how many emblems the pip crop has to hold."""
    spec = (getattr(card_def, "extra_attributes", None) or {}).get(
        str(AttrID.ENERGY_INFO.value))
    if not isinstance(spec, dict):
        return 1
    try:
        options = json.loads(spec.get("value") or "{}").get("options") or []
    except (ValueError, TypeError):
        return 1
    return max((len(option) for option in options), default=1)


def _generate_pip_png(png_path, set_code, asset_name, suffix, detect,
                      art_window=(0.12, 0.68), out_dir=None, units=1):
    out_dir = out_dir or PIP_CACHE_DIR
    out_path = os.path.join(out_dir, f"{set_code}_{asset_name}_{suffix}.png")
    # Regenerate when the source art OR this module (the crop logic) changes.
    stale_after = max(os.path.getmtime(png_path), os.path.getmtime(__file__))
    if os.path.exists(out_path) and os.path.getmtime(out_path) >= stale_after:
        return out_path
    os.makedirs(out_dir, exist_ok=True)
    img = Image.open(png_path).convert("RGBA")
    w, h = img.size
    # Keep the crop inside the art window (title above, text box below).
    art_top, art_bottom = int(h * art_window[0]), int(h * art_window[1])
    circles = _detect_emblem_circles(img, limit=max(1, units)) if detect else []
    if circles:
        # The square that holds every emblem found -- one for most cards, the
        # pair for a two-unit Energy whose art prints two. A pair already
        # fills the frame, so it gets a thinner margin than a lone emblem;
        # 1.16 around two balls reaches the title bar and the name plate.
        margin = 1.16 if len(circles) == 1 else 1.02
        # A pair spans most of the art, so its square lands hard against the
        # window edges. Pull the bottom up for that case only: the name plate
        # sits just under 0.68h on the older frames (Double Dragon Energy) and
        # bleeds into the crop otherwise. Single-emblem pips keep the window
        # they have always used.
        lo = art_top
        hi = art_bottom if len(circles) == 1 else int(h * 0.64)
        left_edge = min(cx - r for cx, _, r in circles)
        right_edge = max(cx + r for cx, _, r in circles)
        top_edge = max(min(cy - r for _, cy, r in circles), lo)
        bottom_edge = min(max(cy + r for _, cy, r in circles), hi)
        art_top, art_bottom = lo, hi
        cx = (left_edge + right_edge) / 2
        cy = (top_edge + bottom_edge) / 2
        side = int(max(right_edge - left_edge, bottom_edge - top_edge) * margin)
    else:
        cx, cy, side = w / 2, (art_top + art_bottom) / 2, art_bottom - art_top
    # Leave the pair case a sliver of room inside the window: at exactly the
    # window height the square is pinned to art_top and picks up the bottom
    # edge of the title bar.
    room = art_bottom - art_top
    side = min(side, w, room if len(circles) <= 1 else int(room * 0.94))
    left = int(min(max(cx - side / 2, 0), w - side))
    top = int(min(max(cy - side / 2, art_top), art_bottom - side))
    img.crop((left, top, left + side, top + side)).save(out_path)
    return out_path


def generate_energy_pip_png(png_path, set_code, asset_name, out_dir=None,
                            units=1):
    """Square crop around the card's circular emblem for the attachment pip.

    The in-match pip requests bundle asset "{set}/{num}_energypip" for special
    energies (EnergyPipTextureRenderer); without it the type symbol shows.

    `units` is how much Energy the card provides at once. The client draws
    exactly one pip per attached card and picks its texture from
    EnergyProvided[0], so a two-unit Energy cropped to a single emblem is
    indistinguishable on the board from a one-unit Energy of the same type.
    Widening the crop to the emblems the art already prints is the only way
    to tell them apart, since the pip count is the client's to decide.
    """
    return _generate_pip_png(png_path, set_code, asset_name, "energypip",
                             detect=True, out_dir=out_dir, units=units)


def generate_tool_pip_png(png_path, set_code, asset_name, out_dir=None):
    """Art-window crop for an attached tool's pip.

    ToolPipTextureRenderer requests "{set}/{num}_toolpip" for every attached
    tool; without it the generic wrench icon shows. Tool art has no fixed
    emblem shape, so the crop is a centered window (no detection). The band
    0.21-0.51h is text-free on BOTH tool layouts: regular tools put the
    "Pokemon Tool" reminder box at ~0.52h, full-arts put it at ~0.14-0.20h.
    """
    return _generate_pip_png(png_path, set_code, asset_name, "toolpip",
                             detect=False, art_window=(0.21, 0.51),
                             out_dir=out_dir)


def check_and_generate_bundles() -> int:
    """
    Scans the loaded card scripts, groups them by set, and generates
    one Unity AssetBundle per set if missing or incomplete. Also compiles cosmetics.
    """
    logging.info("[AutoBundle] Compiling cosmetic bundles...")
    try:
        compile_all_cosmetics()
    except Exception as e:
        logging.error(f"[AutoBundle] Failed to compile cosmetics: {e}")

    logging.info("[AutoBundle] Checking custom landing-page artwork...")
    try:
        dynamic_pages.compile_custom_landing_bundle()
    except Exception as e:
        logging.error(f"[AutoBundle] Failed to compile custom landing pages: {e}")

    logging.info("[AutoBundle] Checking for missing card AssetBundles...")
    
    if not os.path.exists(DEFAULT_TEMPLATE):
        logging.warning(f"[AutoBundle] Template not found: {DEFAULT_TEMPLATE}. Cannot auto-generate bundles.")
        return -1

    if not os.path.exists(BUNDLE_CACHE_DIR):
        os.makedirs(BUNDLE_CACHE_DIR, exist_ok=True)

    if not loader.cards:
        loader.load_all()

    # Group cards by set_code
    sets = {} # set_code -> {coll_num_str: {asset_name: png_path}}
    foil_sets = {} # set_code -> {kind: {padded_num: png_path}}

    scripts_dir = loader.scripts_dir
    for root, _, files in os.walk(scripts_dir):
        for file in files:
            if file.endswith(".py") and file != "__init__.py":
                rel_dir = os.path.relpath(root, scripts_dir)
                base_name = file[:-3]
                png_path = os.path.join(CARDS_IMG_DIR, rel_dir, f"{base_name}.png")
                
                try:
                    file_path = os.path.join(root, file)
                    module_name = "autobundle_" + rel_dir.replace(os.path.sep, "_") + "_" + base_name
                    spec = importlib.util.spec_from_file_location(module_name, file_path)
                    if spec is None or spec.loader is None:
                        continue
                    module = importlib.util.module_from_spec(spec)
                    spec.loader.exec_module(module)
                    if not hasattr(module, 'card'):
                        continue
                    
                    card_def = module.card
                    set_code = card_def.set_code
                    asset_name = str(card_def.collector_number).zfill(3)
                    
                    if set_code not in sets:
                        sets[set_code] = {}
                    
                    card_assets = {asset_name: png_path}

                    # Foil masks live in their own {SET}_wp_{kind}_Foil2 bundles
                    # with textures named by padded number: the client's request
                    # "{SET}_wp_std_Foil2/127" strips to LoadAsset("127"), so a
                    # mask inside the set bundle can never be reached.
                    for suffix, kind in FOIL_KIND_SUFFIXES.items():
                        foil_png_path = os.path.join(CARDS_IMG_DIR, rel_dir, f"{base_name}{suffix}.png")
                        if os.path.exists(foil_png_path):
                            foil_sets.setdefault(set_code, {}).setdefault(kind, {})[asset_name] = foil_png_path

                    # foil-flagged cards with no extracted/hand-authored mask
                    # get a generated one (explicit _foil PNGs above win)
                    foil_def = getattr(card_def, "foil", None)
                    if foil_def is not None and os.path.exists(png_path):
                        style = foil_def.resolve_style(
                            getattr(card_def, "rarity", None),
                            getattr(card_def, "subtypes", None))
                        kinds = [foil_def.mask_kind()]
                        if len(foil_def.effects) > 1:
                            kinds.append("secondary")
                        for kind in kinds:
                            kind_map = foil_sets.setdefault(set_code, {}).setdefault(kind, {})
                            if asset_name in kind_map:
                                continue
                            gen_path = ensure_generated_mask(png_path, set_code, asset_name, kind, style)
                            if gen_path:
                                kind_map[asset_name] = gen_path

                    if _is_special_energy(card_def) and os.path.exists(png_path):
                        pip_path = generate_energy_pip_png(
                            png_path, set_code, asset_name,
                            units=_energy_units(card_def))
                        if pip_path:
                            card_assets[f"{asset_name}_energypip"] = pip_path
                    elif _is_pokemon_tool(card_def) and os.path.exists(png_path):
                        pip_path = generate_tool_pip_png(png_path, set_code, asset_name)
                        if pip_path:
                            card_assets[f"{asset_name}_toolpip"] = pip_path

                    sets[set_code][asset_name] = card_assets

                except Exception as e:
                    logging.error(f"[AutoBundle] Failed to parse {file}: {e}")

    generated_count = 0

    for set_code, cards_dict in sets.items():
        # Merge all card assets for this set into one mapping
        set_mapping = {}
        for coll_num, card_assets in cards_dict.items():
            set_mapping.update(card_assets)

        generated_count += self_generate_set_bundle(set_code, set_mapping)

    generated_count += generate_foil_bundles(foil_sets)

    logging.info(f"[AutoBundle] Scan complete. Generated/Updated: {generated_count} set bundles.")
    return generated_count
