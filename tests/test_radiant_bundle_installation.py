"""Native RC slots must never collide with main-set collector numbers."""
import tempfile
import unittest
import zipfile
from pathlib import Path
from unittest.mock import patch

from spirit.tools import ptcgo_local_assets as installer


class RadiantBundleInstallationTests(unittest.TestCase):
    def test_native_collector_slots(self):
        for code, printed, expected in (
                ('BW11', 'RC1', 116), ('BW11', 'RC25', 140),
                ('TwentiethAnn', 'RC1', 101), ('TwentiethAnn', 'RC32', 132)):
            with self.subTest(code=code, printed=printed):
                self.assertEqual(installer._native_collector(code, printed), expected)
                self.assertEqual(installer._collector_from_script(code, f'Card_{printed}'), expected)
                self.assertEqual(installer._collector_key_from_script(code, f'Card_{printed}'), str(expected))
        self.assertEqual(installer._collector_from_script('BW11', 'Snivy_5'), 5)
        self.assertIsNone(installer._collector_from_script('BW11', 'Invalid_RC26'))

    def make_source(self, root):
        scripts = root / 'scripts'
        (scripts / 'BW11').mkdir(parents=True)
        (scripts / 'BW11' / 'Snivy_RC1.py').touch()
        (scripts / 'BW11' / 'Snivy_5.py').touch()
        with zipfile.ZipFile(root / installer.CARD_ARCHIVES['BW11'], 'w') as archive:
            archive.writestr('bw11/001.png', b'wrong-main-print')
            archive.writestr('bw11/005.png', b'main-print')
            archive.writestr('bw11/116.png', b'native-rc-print')
        return scripts, root / 'art'

    def test_single_card_import_uses_rc_slot(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            self.make_source(root)
            destination = root / 'snivy.png'
            self.assertTrue(installer.install_card_art('BW11', 'RC1', destination, root))
            self.assertEqual(destination.read_bytes(), b'native-rc-print')

    def test_full_archive_import_does_not_skip_rc(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            scripts, assets = self.make_source(root)
            with patch.object(installer, 'CARD_SCRIPT_DIR', scripts), \
                    patch.object(installer, 'CARD_ASSET_DIR', assets):
                totals = installer.import_card_art(root)
            self.assertEqual(totals['written'], 2)
            self.assertEqual((assets / 'BW11/Snivy_RC1.png').read_bytes(), b'native-rc-print')
            self.assertEqual((assets / 'BW11/Snivy_5.png').read_bytes(), b'main-print')

    def test_cache_lookup_uses_native_rc_slot(self):
        with tempfile.TemporaryDirectory() as tmp:
            destination = Path(tmp) / 'snivy.png'
            with patch.object(installer, '_cached_set_art', return_value={
                    '1': b'wrong', '116': b'correct'}) as cache:
                self.assertTrue(installer.install_card_art('BW11', 'RC1', destination, tmp))
            self.assertEqual(destination.read_bytes(), b'correct')
            cache.assert_called_once()

    def test_targeted_import_limits_masks_and_prefers_newer_cache(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            scripts, assets = self.make_source(root)
            for name in ('BW Cache.zip', 'SM Cache.zip'):
                (root / name).touch()
            with patch.object(installer, 'CARD_SCRIPT_DIR', scripts), \
                    patch.object(installer, 'CARD_ASSET_DIR', assets), \
                    patch('spirit.tools.import_foil_masks.extract_set', return_value=(1, 0)) as masks:
                totals = installer.import_radiant_collections(root)
            self.assertEqual(totals['written'], 1)
            self.assertFalse((assets / 'BW11/Snivy_5.png').exists())
            masks.assert_called_once_with('BW11',
                [str(root / 'BW Cache.zip'), str(root / 'SM Cache.zip')],
                force=True, only_cards=list(range(116, 141)))

    def test_default_and_cards_only_include_radiant_but_ui_only_does_not(self):
        for flags, expected in (([], 1), (['--cards-only'], 1), (['--ui-only'], 0),
                                (['--radiant-only'], 1)):
            with self.subTest(flags=flags), tempfile.TemporaryDirectory() as tmp:
                with patch('sys.argv', ['installer', '--source', tmp, *flags]), \
                        patch.object(installer, 'import_radiant_collections', return_value={
                            'written': 0, 'unchanged': 1, 'masks_written': 1, 'unavailable': 0}) as rc, \
                        patch.object(installer, 'import_card_art', return_value={
                            'written': 0, 'unchanged': 0, 'unavailable': 0}), \
                        patch.object(installer, 'import_ui_bundles', return_value={
                            'bundles': 0, 'written': 0, 'unchanged': 0}), \
                        patch.object(installer, 'seed_original_landing_pages', return_value=0), \
                        patch('spirit.tools.install_recent_card_art.install_native_energy', return_value=[]):
                    self.assertEqual(installer.main(), 0)
                    self.assertEqual(rc.call_count, expected)
