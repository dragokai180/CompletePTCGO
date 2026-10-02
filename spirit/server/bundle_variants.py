"""Type-specific card bundles and persistent cache for generated variants."""

import copy
import hashlib
import json
import logging
import os
from pathlib import Path
import re
import tempfile
import threading

from spirit.game.attributes import AttrID, CardType, PokemonTypes


REVISION = 1
SPLIT_TYPES = tuple(t.name.lower() for t in PokemonTypes if 1 <= t.value <= 11) + ("trainer",)


def card_partitions():
    """Map each numbered card image to the types allowed in a virtual bundle."""
    from spirit.game.scripts.cards import loader

    result = {}
    for card in loader.load_all():
        get = card.get_attribute_value
        set_code = get(AttrID.SET_KEY)
        number = str(get(AttrID.IMAGE_URL, ""))
        if not set_code or not number.isdigit():
            continue
        if get(AttrID.CARD_TYPE) == CardType.TRAINER:
            kinds = ["trainer"]
        else:
            types = get(AttrID.POKEMON_TYPES, "[]")
            types = json.loads(types) if isinstance(types, str) else types
            kinds = [PokemonTypes(t).name.lower() for t in types if t in range(1, 12)]
            kinds = kinds or ["colorless"]
        result.setdefault(set_code, {}).setdefault(int(number), set()).update(kinds)
    return result


def asset_number(name, set_code):
    name = name.lower()
    for prefix in (set_code.lower() + "/", set_code.lower() + "_"):
        if name.startswith(prefix):
            name = name[len(prefix):]
            break
    match = re.fullmatch(r"(?:foil_)?(\d+)(?:_energypip|_energyicon|_toolpip)?", name)
    return int(match[1]) if match else None


def variant_version(source, membership):
    stat = os.stat(source)
    payload = [REVISION, stat.st_size, stat.st_mtime_ns,
               [(number, sorted(kinds)) for number, kinds in sorted(membership.items())]]
    return int.from_bytes(hashlib.sha256(json.dumps(payload).encode()).digest()[:4], "big") & 0x7fffffff


def trim_textures(env, set_code, kind, membership):
    """Remove other types only from self-contained texture bundles.

    Unknown image keys, including combined V-UNION faces, are retained.
    """
    objects = list(env.objects)
    if len(env.assets) != 1 or any(obj.type.name not in ("Texture2D", "AssetBundle") for obj in objects):
        return False
    bundles = [obj for obj in objects if obj.type.name == "AssetBundle"]
    if len(bundles) != 1 or env.assets[0].externals:
        return False
    bundle = bundles[0].read()
    textures = {obj.path_id: obj for obj in objects if obj.type.name == "Texture2D"}
    if any(getattr(obj.read(), "m_StreamData", None) and obj.read().m_StreamData.path
           for obj in textures.values()):
        return False
    by_id = {}
    for name, info in bundle.m_Container:
        by_id.setdefault(info.asset.m_PathID, set()).add(asset_number(name, set_code))
    remove = {pid for pid, numbers in by_id.items()
              if pid in textures and numbers and
              all(number in membership and kind not in membership[number] for number in numbers)}
    if not remove:
        return False
    bundle.m_Container = [(name, info) for name, info in bundle.m_Container
                          if info.asset.m_PathID not in remove]
    preload = []
    for _, info in bundle.m_Container:
        info.preloadIndex = len(preload)
        info.preloadSize = 1
        preload.append(copy.copy(info.asset))
    bundle.m_PreloadTable = preload
    main = getattr(bundle, "m_MainAsset", None)
    if main is not None and main.asset.m_PathID in remove:
        main.asset.m_PathID = 0
        main.preloadIndex = main.preloadSize = 0
    bundles[0].save_typetree(bundle)
    for pid in remove:
        del env.assets[0].objects[pid]
    return True


class DiskBundleCache:
    def __init__(self, directory, max_bytes):
        self.directory = Path(directory)
        self.max_bytes = max(0, max_bytes)
        self.lock = threading.Lock()

    def _path(self, key):
        return self.directory / (hashlib.sha256(key.encode()).hexdigest() + ".bundle")

    def get(self, key):
        if not self.max_bytes:
            return None
        try:
            path = self._path(key)
            size = path.stat().st_size
            if not 0 < size <= self.max_bytes:
                return None
            data = path.read_bytes()
            if len(data) != size:
                return None
            path.touch()
            return data
        except OSError:
            return None

    def put(self, key, data):
        if not self.max_bytes or len(data) > self.max_bytes:
            return
        temporary = None
        try:
            with self.lock:
                self.directory.mkdir(parents=True, exist_ok=True)
                with tempfile.NamedTemporaryFile(dir=self.directory, suffix=".tmp", delete=False) as output:
                    temporary = Path(output.name)
                    output.write(data)
                target = self._path(key)
                os.replace(temporary, target)
                files = [(path.stat().st_mtime_ns, path.stat().st_size, path)
                         for path in self.directory.glob("*.bundle")]
                total = sum(size for _, size, _ in files)
                for _, size, path in sorted(files):
                    if total <= self.max_bytes:
                        break
                    if path == target:
                        continue
                    try:
                        path.unlink()
                        total -= size
                    except OSError:
                        pass
        except OSError as exc:
            logging.warning("[HTTP] Cannot persist bundle cache: %s", exc)
        finally:
            if temporary is not None:
                try:
                    temporary.unlink(missing_ok=True)
                except OSError:
                    pass
