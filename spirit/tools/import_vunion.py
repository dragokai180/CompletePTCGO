"""Import the original 20 V-UNION parts and five combined faces from PTCGO.

Usage: python -m spirit.tools.import_vunion --source A:/PTCGO
No downloaded/reconstructed art or inferred foil mask is used.
"""
import argparse
from pathlib import Path
from zipfile import ZipFile

import UnityPy
from PIL import Image

from spirit.game.vunion import SPECS
from spirit.tools.import_foil_masks import _bundle_payloads, KIND_SUFFIXES
from spirit.tools import ptcgo_local_assets as native


def import_vunion(source, *, destination=None):
    """Install and verify all faces and standard masks, including composites.

    Existing valid assets count on reruns; an incomplete cache must not report
    success just because all four individual pieces of a Pokemon were found.
    """
    destination = Path(destination) if destination is not None else native.CARD_ASSET_DIR / 'Promo_SWSH'
    destination.mkdir(parents=True, exist_ok=True)
    stems = {}
    for name, (start, *_) in SPECS.items():
        for number in range(start, start + 4):
            stems[str(number)] = f'{name}VUNION_{number}'
        stems[f'{start}to{start + 3}'] = f'{name}VUNION_combined'
    found, masks = set(), set()
    caches = list(reversed(native._cache_archives(Path(source))))
    for cache in caches:
        with ZipFile(cache) as archive:
            for name, spec in SPECS.items():
                token = f'/en_US_Promo_SWSH_{spec[-1]}/'
                for member in archive.namelist():
                    if token not in member or not member.endswith('/__data'):
                        continue
                    env = UnityPy.load(archive.read(member))
                    for obj in env.objects:
                        if obj.type.name != 'Texture2D':
                            continue
                        texture = obj.read()
                        stem = stems.get(texture.m_Name)
                        if stem is not None:
                            texture.image.save(destination / f'{stem}.png')
                            found.add(texture.m_Name)
        for kind, suffix in KIND_SUFFIXES.items():
            for bundle in _bundle_payloads(str(cache), 'Promo_SWSH', kind):
                env = UnityPy.load(bundle.load_arg())
                for obj in env.objects:
                    if obj.type.name != 'Texture2D':
                        continue
                    texture = obj.read()
                    stem = stems.get(texture.m_Name)
                    if stem is not None:
                        texture.image.save(destination / f'{stem}{suffix}.png')
                        masks.add((texture.m_Name, kind))
    missing = []
    for stem in stems.values():
        for suffix in ('', '_foil'):
            path = destination / f'{stem}{suffix}.png'
            try:
                with Image.open(path) as image:
                    image.verify()
            except (OSError, ValueError, SyntaxError):
                missing.append(path.name)
    print(f'V-UNION: {len(found)} native faces imported; {len(masks)} exact native masks imported; '
          f'{50 - len(missing)}/50 required files installed.')
    for name in missing:
        print(f'[V-UNION] Missing or invalid: {name}')
    return missing


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--source', help='Local cbrew folder; defaults to PTCGO_ART_SOURCE_DIR')
    args = parser.parse_args()
    source = native.source_directory(args.source)
    if not source.is_dir():
        parser.error(f'PTCGO asset directory does not exist: {source}')
    return 2 if import_vunion(source) else 0


if __name__ == '__main__':
    raise SystemExit(main())
