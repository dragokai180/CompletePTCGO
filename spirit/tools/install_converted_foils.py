"""Install pre-converted PTCGO foil bundles, not the raw TCG Live cache.

Run from the repository root, with the server stopped:
    python -m spirit.tools.install_converted_foils --source PATH

PATH is the exported PGO-CRZLiveBundles directory or a ZIP of that directory.
Only masks are installed; card faces, accounts and configuration are untouched.
"""
from __future__ import annotations

import argparse
from pathlib import Path
import zipfile

from spirit.tools import import_foil_masks as masks

SETS = ('PGO', 'SWSH11', 'SWSH12', 'CZ')
REQUIRED_KINDS = ('std', 'ph', 'secondary')


def install(source: Path, sets=SETS) -> int:
    source = source.expanduser().resolve()
    if not source.is_dir() and not (source.is_file() and zipfile.is_zipfile(source)):
        raise ValueError('Source must be a converted-bundle directory or ZIP archive.')
    if not sets or any(code not in SETS for code in sets):
        raise ValueError('Supported sets: ' + ', '.join(SETS))
    # Check the entire selection before modifying any installed masks.
    missing = [f'en_US_{code}_wp_{kind}_Foil2' for code in sets
               for kind in REQUIRED_KINDS
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
    # Keep decoded originals beside card art. Startup can then rebuild bundles
    # without reverting the installation or pruning the imported masks.
    return total


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--source', type=Path, required=True,
                        help='Converted PGO-CRZLiveBundles directory or ZIP (not raw Live cache)')
    parser.add_argument('--sets', nargs='+', choices=SETS, default=list(SETS),
                        help='Optional subset; defaults to all four collections')
    args = parser.parse_args()
    try:
        count = install(args.source, args.sets)
    except Exception as exc:
        print(f'[converted-foils] Installation failed: {exc}')
        print('Fix the source and rerun; a failed run is not a complete installation.')
        return 2
    print(f'[converted-foils] Installed {count} original converted masks.')
    print('Start/restart the server to rebuild its foil bundles; reconnect the clients.')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
