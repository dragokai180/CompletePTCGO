"""Install pre-converted PTCGO foil bundles, not the raw TCG Live cache.

Run from the repository root, with the server stopped:
    python -m spirit.tools.install_converted_foils --source PATH

PATH is the exported PGO-CRZLiveBundles directory or a ZIP of that directory.
The pack may also include a verified metadata overlay and composite V-UNION
artwork required by an imported foil. Accounts and user configuration are
never touched.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import shutil
import zipfile

from spirit.tools import import_foil_masks as masks

PACK_KINDS = {
    # Original PGO-to-Crown-Zenith converted pack.
    'PGO': ('std', 'ph', 'secondary'),
    'SWSH11': ('std', 'ph', 'secondary'),
    'SWSH12': ('std', 'ph', 'secondary'),
    'CZ': ('std', 'ph', 'secondary'),
    # Missing known foils imported from the Live cache. Reverse masks are
    # deliberately absent: they are archived, but are not enabled in Spirit.
    'BW11': ('std',),
    'SM5': ('std',),
    'SM7': ('std',),
    'SM10': ('std',),
    'SM12': ('std',),
    'Promo_SM': ('std',),
    'CEL25': ('std', 'secondary'),
    'Promo_SWSH': ('std',),
}
SETS = tuple(PACK_KINDS)
BASE_SETS = ('PGO', 'SWSH11', 'SWSH12', 'CZ')
REQUIRED_KINDS = ('std', 'ph', 'secondary')
MANIFEST_FILE = 'converted_foils_manifest.json'


def _source_member(source: Path, name: str):
    """Return bytes for a pack companion file, including ZIPs with a wrapper."""
    if source.is_dir():
        path = source / name
        return path.read_bytes() if path.is_file() else None
    with zipfile.ZipFile(source) as archive:
        matches = [entry for entry in archive.namelist()
                   if entry.replace('\\', '/').rstrip('/').endswith('/' + name)
                   or entry.replace('\\', '/').rstrip('/') == name]
        if len(matches) > 1:
            raise ValueError(f'Ambiguous companion file in converted pack: {name}')
        return archive.read(matches[0]) if matches else None


def _read_manifest(source: Path) -> dict:
    raw = _source_member(source, MANIFEST_FILE)
    if raw is None:
        return {}
    try:
        manifest = json.loads(raw.decode('utf-8'))
    except (UnicodeDecodeError, json.JSONDecodeError) as exc:
        raise ValueError(f'Invalid {MANIFEST_FILE}: {exc}') from exc
    if not isinstance(manifest, dict) or manifest.get('schema') != 1:
        raise ValueError(f'Unsupported {MANIFEST_FILE} schema')
    return manifest


def _apply_manifest_extras(source: Path, manifest: dict) -> None:
    """Install only explicitly listed local assets after mask extraction."""
    root = Path('spirit/assets').resolve()
    for item in manifest.get('assets', []):
        if not isinstance(item, dict):
            raise ValueError('Invalid companion asset entry')
        source_name, relative, expected = item.get('source'), item.get('target'), item.get('sha256')
        if not all(isinstance(value, str) for value in (source_name, relative, expected)):
            raise ValueError('Invalid companion asset metadata')
        if Path(relative).is_absolute() or '..' in Path(relative).parts:
            raise ValueError(f'Unsafe companion asset target: {relative}')
        data = _source_member(source, source_name)
        if data is None:
            raise ValueError(f'Missing companion asset: {source_name}')
        if hashlib.sha256(data).hexdigest() != expected:
            raise ValueError(f'Checksum mismatch for companion asset: {source_name}')
        target = (root / relative).resolve()
        if root not in target.parents:
            raise ValueError(f'Companion asset escapes assets directory: {relative}')
        target.parent.mkdir(parents=True, exist_ok=True)
        staged = target.with_suffix(target.suffix + '.new')
        staged.write_bytes(data)
        staged.replace(target)


def _apply_metadata_overlay(source: Path, manifest: dict) -> None:
    name = manifest.get('metadata_overlay')
    if name is None:
        return
    if not isinstance(name, str) or Path(name).name != name:
        raise ValueError('Invalid metadata overlay name')
    raw = _source_member(source, name)
    if raw is None:
        raise ValueError(f'Missing metadata overlay: {name}')
    try:
        overlay = json.loads(raw.decode('utf-8'))
    except (UnicodeDecodeError, json.JSONDecodeError) as exc:
        raise ValueError(f'Invalid metadata overlay: {exc}') from exc
    if not isinstance(overlay, dict) or not all(isinstance(v, dict) for v in overlay.values()):
        raise ValueError('Invalid metadata overlay structure')
    target = Path('spirit/game/foil_metadata.json')
    metadata = json.loads(target.read_text(encoding='utf-8'))
    for set_code, records in overlay.items():
        metadata.setdefault(set_code, {}).update(records)
    staged = target.with_suffix('.json.new')
    staged.write_text(json.dumps(metadata, ensure_ascii=False, separators=(',', ':')), encoding='utf-8')
    staged.replace(target)


def install(source: Path, sets=None) -> int:
    source = source.expanduser().resolve()
    if not source.is_dir() and not (source.is_file() and zipfile.is_zipfile(source)):
        raise ValueError('Source must be a converted-bundle directory or ZIP archive.')
    manifest = _read_manifest(source)
    # Existing PGO-CRZ packs did not carry a manifest. Keep their historical
    # four-set default, while MissingBundles opts into all available exports.
    if sets is None:
        sets = SETS if manifest else BASE_SETS
    if not sets or any(code not in SETS for code in sets):
        raise ValueError('Supported sets: ' + ', '.join(SETS))
    # Check the entire selection before modifying any installed masks.
    missing = [f'en_US_{code}_wp_{kind}_Foil2' for code in sets
               for kind in PACK_KINDS[code]
               if not masks._bundle_payloads(str(source), code, kind)]
    if missing:
        raise ValueError('Incomplete converted bundle pack; missing: ' + ', '.join(missing))
    total = 0
    for code in dict.fromkeys(sets):
        written, _ = masks.extract_set(code, [str(source)], force=True,
                                      strict=True, container_only=True)
        if not written:
            raise ValueError(f'{code}: no masks installed. Check the card scripts and pack.')
        total += written
    _apply_metadata_overlay(source, manifest)
    _apply_manifest_extras(source, manifest)
    # Keep decoded originals beside card art. Startup can then rebuild bundles
    # without reverting the installation or pruning the imported masks.
    return total


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--source', type=Path, required=True,
                        help='Converted foil-bundle directory or ZIP (not raw Live cache)')
    parser.add_argument('--sets', nargs='+', choices=SETS,
                        help='Optional subset; defaults to the collections supplied by the pack')
    args = parser.parse_args()
    try:
        count = install(args.source, args.sets)
    except Exception as exc:
        print(f'[converted-foils] Installation failed: {exc}')
        print('Fix the source and rerun; a failed run is not a complete installation.')
        return 2
    print(f'[converted-foils] Installed {count} original converted masks and companion data.')
    print('Start/restart the server to rebuild its foil bundles; reconnect the clients.')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
