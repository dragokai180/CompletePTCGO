"""Native V-UNION installation includes complete faces and exact foil masks."""
import tempfile
import unittest
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import patch
from zipfile import ZipFile

from PIL import Image
from spirit.tools import import_vunion as vunion
from spirit.tools import ptcgo_local_assets as installer
from spirit.tools import install_recent_card_art as downloader


def texture_objects(mask=False):
    textures = []
    for name, spec in vunion.SPECS.items():
        start = spec[0]
        for number in [*(str(n) for n in range(start, start + 4)), f'{start}to{start + 3}']:
            texture = SimpleNamespace(m_Name=number, image=Image.new('RGBA', (8, 8),
                                      'white' if mask else 'blue'))
            textures.append(SimpleNamespace(type=SimpleNamespace(name='Texture2D'),
                                           read=lambda t=texture: t))
    return SimpleNamespace(objects=textures)


class VUnionInstallationTests(unittest.TestCase):
    def test_native_cache_installs_all_parts_combined_faces_and_masks(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            output = root / 'art'
            with ZipFile(root / 'SM Cache.zip', 'w') as archive:
                for spec in vunion.SPECS.values():
                    archive.writestr(f'cache/en_US_Promo_SWSH_{spec[-1]}/revision/__data', b'faces')
            def masks(cache, code, kind):
                self.assertEqual(code, 'Promo_SWSH')
                return [SimpleNamespace(load_arg=lambda: b'masks')] if kind == 'std' else []
            with patch.object(vunion, '_bundle_payloads', side_effect=masks), \
                    patch.object(vunion.UnityPy, 'load', side_effect=lambda data: texture_objects(data == b'masks')), \
                    patch('builtins.print'):
                self.assertEqual(vunion.import_vunion(root, destination=output), [])
                self.assertEqual(vunion.import_vunion(root, destination=output), [])
            self.assertEqual(len(list(output.glob('*.png'))), 50)
            for name in vunion.SPECS:
                for suffix in ('', '_foil'):
                    self.assertTrue((output / f'{name}VUNION_combined{suffix}.png').is_file())

    def test_missing_combined_face_and_mask_are_errors_even_when_parts_exist(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            output = root / 'art'
            output.mkdir()
            for name, spec in vunion.SPECS.items():
                for tail in [*range(spec[0], spec[0] + 4), 'combined']:
                    for suffix in ('', '_foil'):
                        if name == 'Mewtwo' and tail == 'combined':
                            continue
                        Image.new('RGBA', (8, 8)).save(output / f'{name}VUNION_{tail}{suffix}.png')
            with patch('builtins.print'):
                self.assertEqual(sorted(vunion.import_vunion(root, destination=output)),
                                 ['MewtwoVUNION_combined.png', 'MewtwoVUNION_combined_foil.png'])
            (output / 'MewtwoVUNION_combined.png').write_bytes(b'not an image')
            with patch('builtins.print'):
                self.assertEqual(len(vunion.import_vunion(root, destination=output)), 2)

    def test_default_cards_only_and_targeted_install_include_vunion(self):
        for flags, expected in (([], 1), (['--cards-only'], 1), (['--vunion-only'], 1),
                                (['--ui-only'], 0), (['--radiant-only'], 0),
                                (['--premium-xy-only'], 0)):
            for missing in ([], ['MewtwoVUNION_combined_foil.png']):
                with self.subTest(flags=flags, missing=missing), tempfile.TemporaryDirectory() as tmp, \
                        patch('sys.argv', ['installer', '--source', tmp, *flags]), \
                        patch.object(vunion, 'import_vunion', return_value=missing) as imported, \
                        patch.object(installer, 'import_premium_xy_foils', return_value={'written': 14, 'missing': [], 'available': True}), \
                        patch.object(installer, 'import_radiant_collections', return_value={'written': 0, 'unchanged': 0, 'masks_written': 0, 'unavailable': 0}), \
                        patch.object(installer, 'import_card_art', return_value={'written': 0, 'unchanged': 0, 'unavailable': 0}) as cards, \
                        patch.object(installer, 'import_ui_bundles', return_value={'bundles': 0, 'written': 0, 'unchanged': 0}), \
                        patch.object(installer, 'seed_original_landing_pages', return_value=0), \
                        patch('spirit.tools.install_recent_card_art.install_native_energy', return_value=[]), \
                        patch('builtins.print'):
                    self.assertEqual(installer.main(), 2 if expected and missing else 0)
                    self.assertEqual(imported.call_count, expected)
                    if expected:
                        imported.assert_called_once_with(Path(tmp))
                    if '--vunion-only' in flags:
                        cards.assert_not_called()

    def test_targeted_import_rejects_conflicting_flags(self):
        for flag in ('--ui-only', '--radiant-only', '--premium-xy-only'):
            with tempfile.TemporaryDirectory() as tmp, \
                    patch('sys.argv', ['installer', '--source', tmp, '--vunion-only', flag]), \
                    patch.object(vunion, 'import_vunion') as imported, \
                    patch('sys.stderr'):
                with self.assertRaises(SystemExit) as result:
                    installer.main()
                self.assertEqual(result.exception.code, 2)
                imported.assert_not_called()

    def test_standalone_import_uses_configured_source(self):
        with tempfile.TemporaryDirectory() as tmp, \
                patch.dict('os.environ', {installer.SOURCE_ENV: tmp}), \
                patch('sys.argv', ['import_vunion']), \
                patch.object(vunion, 'import_vunion', return_value=[]) as imported:
            self.assertEqual(vunion.main(), 0)
            imported.assert_called_once_with(Path(tmp))

    def test_download_installer_discovers_all_twenty_physical_prints(self):
        with tempfile.TemporaryDirectory() as tmp, \
                patch.object(downloader, 'ASSETS_ROOT', Path(tmp)), \
                patch.object(downloader, 'load_image_urls', return_value={}):
            tasks = downloader.build_tasks(downloader.RECENT_SETS['swshp'])
        physical = [destination for _, destination in tasks if 'VUNION' in destination.name]
        self.assertEqual(len(physical), 20)
        self.assertTrue(all('combined' not in p.name for p in physical))


if __name__ == '__main__':
    unittest.main()
