"""Repair card textures made by older create_card_bundle.py versions.

Those versions cloned the template AssetInfo without adding a preload pointer
for each new Texture2D. UnityPy can read the texture, but native LoadAsset can
resolve the stale template preload instead of the requested card art.
"""

import argparse
import copy
import os
import tempfile

import UnityPy


def repair(path):
    # UnityPy otherwise keeps the input file open, preventing atomic replace
    # on Windows after the rebuilt bundle is written.
    with open(path, 'rb') as source:
        env = UnityPy.load(source.read())
    bundle_obj = next(obj for obj in env.objects if obj.type.name == 'AssetBundle')
    bundle = bundle_obj.read()
    texture_ids = {obj.path_id for obj in env.objects if obj.type.name == 'Texture2D'}
    new_indices = {}
    repaired = 0

    for _, info in bundle.m_Container:
        path_id = int(info.asset.m_PathID)
        if path_id not in texture_ids:
            continue
        start = info.preloadIndex
        end = start + info.preloadSize
        preload_ids = {int(ptr.m_PathID) for ptr in bundle.m_PreloadTable[start:end]}
        if path_id in preload_ids:
            continue
        if path_id not in new_indices:
            new_indices[path_id] = len(bundle.m_PreloadTable)
            bundle.m_PreloadTable.append(copy.copy(info.asset))
        info.preloadIndex = new_indices[path_id]
        info.preloadSize = 1
        repaired += 1

    if not repaired:
        return 0

    bundle_obj.save_typetree(bundle)
    directory = os.path.dirname(os.path.abspath(path))
    fd, temporary = tempfile.mkstemp(prefix='__data.preload.', dir=directory)
    try:
        with os.fdopen(fd, 'wb') as output:
            output.write(env.file.save(packer='lz4'))
        os.replace(temporary, path)
    finally:
        if os.path.exists(temporary):
            os.remove(temporary)
    return repaired


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('bundles', nargs='+', help='Paths to Unity bundle __data files')
    args = parser.parse_args()
    for bundle_path in args.bundles:
        print(f'{bundle_path}: repaired {repair(bundle_path)} container entries')
