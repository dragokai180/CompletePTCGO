"""Download missing expansion symbols from PokemonSymbols.

The archived PTCGO cache already contains the original ``setIcons`` bundles
through Astral Radiance.  Sets added after the client was discontinued (plus a
few aliases used by this server's SetData) need matching 64 x 64 textures in a
small supplemental bundle.  Keep the source mapping here so adding a future
set is explicit and reproducible.

Run from the repository root::

    python -m spirit.tools.import_set_symbols
    python -m spirit.tools.import_set_symbols --force
"""
from __future__ import annotations

import argparse
import io
import os
import tempfile
from pathlib import Path
from urllib.request import Request, urlopen

from PIL import Image


PROJECT_DIR = Path(__file__).resolve().parents[2]
OUTPUT_DIR = PROJECT_DIR / "spirit" / "assets" / "products" / "custom_seticons"
SOURCE_BASE = "https://pokesymbols.com/images/tcg/sets/symbols"


# Texture name (SetData.name, lower-case) -> PokemonSymbols image slug.
# Energy pseudo-sets reuse their era's symbol; promo groups use the site's
# official Black Star Promo symbol.
SYMBOL_SLUGS = {
    "bw_energy": "black-and-white",
    "hgss_energy": "heartgold-soulsilver",
    "xy_energy": "xy",
    "sm_energy": "sun-and-moon",
    "swsh_energy": "sword-and-shield",
    "tk9a": "xy-trainer-kit-libre-pikachu",
    "tk9b": "xy-trainer-kit-suicune",
    "mcdonalds": "mcdonalds-collection-2011",
    "swsh35": "champions-path",
    "swsh45": "shining-fates",
    "cel25": "celebrations",
    "pgo": "pokemon-go",
    "swsh11": "lost-origin",
    "swsh12": "silver-tempest",
    "cz": "crown-zenith",
    "sve": "scarlet-and-violet-energies",
    "promo_sv": "_promo",
    "svp": "_promo",
    "sv1": "scarlet-and-violet",
    "sv2": "paldea-evolved",
    "sv3": "obsidian-flames",
    "sv035": "151",
    "sv4": "paradox-rift",
    "sv045": "paldean-fates",
    "sv05": "temporal-forces",
    "sv06": "twilight-masquerade",
    "sv065": "shrouded-fable",
    "sv07": "stellar-crown",
    "sv08": "surging-sparks",
    "sv085": "prismatic-evolutions",
    "sv09": "journey-together",
    "sv10": "destined-rivals",
    "rsv10pt5": "white-flare",
    "zsv10pt5": "black-bolt",
    "me1": "mega-evolution",
    "me2": "phantasmal-flames",
    "me2pt5": "ascended-heroes",
    "me3": "perfect-order",
    "me4": "chaos-rising",
    "me5": "pitch-black",
    "mep": "_promo",
}


def symbol_url(slug: str) -> str:
    return f"{SOURCE_BASE}/{slug}.png"


def _download(url: str) -> bytes:
    request = Request(url, headers={"User-Agent": "PobreTCG-set-symbol-importer/1.0"})
    with urlopen(request, timeout=30) as response:
        payload = response.read()
    with Image.open(io.BytesIO(payload)) as image:
        if image.format != "PNG":
            raise ValueError(f"source is not PNG: {url}")
        # A few recent symbols are palette PNGs.  UnityPy's Texture2D packer
        # expects a concrete color mode, so normalize every source before it
        # reaches the supplemental bundle.
        normalized = image.convert("RGBA")
        output = io.BytesIO()
        normalized.save(output, format="PNG")
    return output.getvalue()


def _atomic_write(destination: Path, payload: bytes) -> None:
    destination.parent.mkdir(parents=True, exist_ok=True)
    fd, temporary = tempfile.mkstemp(
        prefix=f".{destination.name}.", suffix=".tmp", dir=destination.parent
    )
    try:
        with os.fdopen(fd, "wb") as output:
            output.write(payload)
        os.replace(temporary, destination)
    finally:
        try:
            os.unlink(temporary)
        except FileNotFoundError:
            pass


def import_symbols(*, force: bool = False) -> dict[str, int]:
    totals = {"downloaded": 0, "kept": 0}
    payloads: dict[str, bytes] = {}
    for texture_name, slug in SYMBOL_SLUGS.items():
        destination = OUTPUT_DIR / f"{texture_name}.png"
        if destination.is_file() and not force:
            totals["kept"] += 1
            continue
        payload = payloads.get(slug)
        if payload is None:
            payload = _download(symbol_url(slug))
            payloads[slug] = payload
        _atomic_write(destination, payload)
        totals["downloaded"] += 1
        print(f"[set-icons] {texture_name} <- {slug}")
    return totals


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Import missing PTCGO expansion symbols from PokemonSymbols."
    )
    parser.add_argument("--force", action="store_true", help="Replace existing PNGs.")
    args = parser.parse_args()
    totals = import_symbols(force=args.force)
    print(
        "[set-icons] complete: "
        f"downloaded={totals['downloaded']}, kept={totals['kept']}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
