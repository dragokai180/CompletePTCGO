"""Validate generated Unity bundles and repair a short serialized-file header."""

import UnityPy


def repair_serialized_file_size(raw):
    """Correct UnityPy's occasional 1-8 byte overstatement in an inner CAB."""
    if len(raw) < 20:
        raise ValueError("Serialized file is too short")
    declared = int.from_bytes(raw[4:8], "big")
    version = int.from_bytes(raw[8:12], "big")
    difference = declared - len(raw)
    if not (1 <= difference <= 8 and 1 <= version <= 21):
        raise ValueError("Serialized file size mismatch is not safely repairable")
    fixed = bytearray(raw)
    fixed[4:8] = len(fixed).to_bytes(4, "big")
    if not UnityPy.load(bytes(fixed)).objects:
        raise ValueError("Corrected serialized file still has no assets")
    return bytes(fixed)


def ensure_asset_bundle(data):
    """Return a parseable card bundle or raise before it is installed."""
    env = UnityPy.load(data)
    if any(obj.type.name == "AssetBundle" for obj in env.objects):
        for obj in env.objects:
            try:
                obj.read()
            except Exception as exc:
                raise ValueError(
                    f"Generated card bundle has unreadable {obj.type.name} "
                    f"at PathID {obj.path_id}"
                ) from exc
        return data
    files = getattr(env.file, "files", None)
    if not files or len(files) != 1:
        raise ValueError("Generated card bundle contains no AssetBundle")
    name, reader = next(iter(files.items()))
    if not hasattr(reader, "bytes"):
        raise ValueError("Generated card bundle contains no readable CAB")
    fixed = repair_serialized_file_size(reader.bytes)
    inner = UnityPy.load(fixed).file
    inner.flags = reader.flags
    inner.name = name
    env.file.files[name] = inner
    repaired = env.file.save(packer="lz4")
    check = UnityPy.load(repaired)
    if not any(obj.type.name == "AssetBundle" for obj in check.objects):
        raise ValueError("Repaired card bundle contains no AssetBundle")
    for obj in check.objects:
        try:
            obj.read()
        except Exception as exc:
            raise ValueError(
                f"Repaired card bundle has unreadable {obj.type.name} "
                f"at PathID {obj.path_id}"
            ) from exc
    return repaired
