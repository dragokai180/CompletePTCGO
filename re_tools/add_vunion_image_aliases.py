"""Add native zoom names for combined V-UNION textures in existing bundles.

The playmat requests ``163to166``; the card zoom requests ``to166``.  Both
names must point at the same Texture2D in the Unity AssetBundle container.
"""

import argparse
import os
import re
import tempfile

import UnityPy


def add_aliases(path):
    with open(path, 'rb') as source:
        env = UnityPy.load(source.read())
    bundle_obj = next(obj for obj in env.objects if obj.type.name == 'AssetBundle')
    bundle = bundle_obj.read()
    prefix = bundle.m_Name.removeprefix('en_US_')
    existing = {name: int(info.asset.m_PathID) for name, info in bundle.m_Container}
    additions = []

    for name, info in tuple(bundle.m_Container):
        match = re.fullmatch(r'\d+to(\d+)', name)
        if not match:
            continue
        zoom = f'to{match.group(1)}'
        for alias in (zoom, f'{prefix}/{zoom}', f'{prefix}_{zoom}'):
            path_id = int(info.asset.m_PathID)
            if alias in existing:
                if existing[alias] != path_id:
                    raise ValueError(f'{alias} already points to another texture')
                continue
            bundle.m_Container.append((alias, info))
            existing[alias] = path_id
            additions.append(alias)

    if not additions:
        return []
    bundle_obj.save_typetree(bundle)
    directory = os.path.dirname(os.path.abspath(path))
    fd, temporary = tempfile.mkstemp(prefix='__data.vunion.', dir=directory)
    try:
        with os.fdopen(fd, 'wb') as output:
            output.write(env.file.save(packer='lz4'))
        os.replace(temporary, path)
    finally:
        if os.path.exists(temporary):
            os.remove(temporary)
    return additions


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('bundles', nargs='+')
    args = parser.parse_args()
    for bundle_path in args.bundles:
        print(bundle_path, add_aliases(bundle_path))
