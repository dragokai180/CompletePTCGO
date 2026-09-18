"""The standard cbrew installation must wire the exact Premium XY import."""
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from spirit.game.foil_variants import PREMIUM_XY_FOIL_VARIANTS
from spirit.tools import ptcgo_local_assets as installer
from spirit.tools import import_foil_masks as masks


class PremiumXYInstallationTests(unittest.TestCase):
    def test_exact_variants_and_native_directory_case(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            scripts, assets = root / 'scripts', root / 'assets'
            scripts.mkdir()
            for name in ('BW Cache.zip', 'SM Cache.zip'):
                (root / name).touch()
            for code in PREMIUM_XY_FOIL_VARIANTS:
                actual = {'PROMO_XY': 'Promo_XY', 'TWENTIETHANN': 'TwentiethAnn'}.get(code, code)
                (scripts / actual).mkdir()
            def extract(code, caches, **kwargs):
                self.assertEqual(caches, [str(root / 'BW Cache.zip'), str(root / 'SM Cache.zip')])
                self.assertEqual(kwargs, {'force': True, 'only_cards': list(PREMIUM_XY_FOIL_VARIANTS[code.upper()])})
                (assets / code).mkdir(parents=True)
                for slot in kwargs['only_cards']:
                    (assets / code / f'Card_{slot}_foil.png').touch()
                return len(kwargs['only_cards']), 0
            with patch.object(installer, 'CARD_SCRIPT_DIR', scripts), \
                    patch.object(installer, 'CARD_ASSET_DIR', assets), \
                    patch.object(masks, 'extract_set', side_effect=extract), \
                    patch.object(masks, '_set_card_stems', side_effect=lambda code: {
                        slot.zfill(3): f'Card_{slot}' for slot in PREMIUM_XY_FOIL_VARIANTS[code.upper()]}):
                self.assertEqual(installer.import_premium_xy_foils(root),
                                 {'written': 14, 'missing': [], 'available': True})
            self.assertTrue((assets / 'Promo_XY').is_dir())
            self.assertTrue((assets / 'TwentiethAnn').is_dir())

    def test_default_and_cards_only_run_import(self):
        for flags, calls in (([], 1), (['--cards-only'], 1), (['--ui-only'], 0),
                             (['--radiant-only'], 0), (['--premium-xy-only'], 1)):
            with self.subTest(flags=flags), tempfile.TemporaryDirectory() as tmp:
                with patch('sys.argv', ['installer', '--source', tmp, *flags]), \
                        patch('spirit.tools.import_vunion.import_vunion', return_value=[]), \
                        patch.object(installer, 'import_premium_xy_foils', return_value={'written': 14, 'missing': [], 'available': True}) as premium, \
                        patch.object(installer, 'import_radiant_collections', return_value={'written': 0, 'unchanged': 0, 'masks_written': 0, 'unavailable': 0}), \
                        patch.object(installer, 'import_card_art', return_value={'written': 0, 'unchanged': 0, 'unavailable': 0}) as cards, \
                        patch.object(installer, 'import_ui_bundles', return_value={'bundles': 0, 'written': 0, 'unchanged': 0}), \
                        patch.object(installer, 'seed_original_landing_pages', return_value=0), \
                        patch('spirit.tools.install_recent_card_art.install_native_energy', return_value=[]):
                    self.assertEqual(installer.main(), 0)
                    self.assertEqual(premium.call_count, calls)
                    if '--premium-xy-only' in flags:
                        cards.assert_not_called()

    def test_targeted_refresh_reports_absent_and_incomplete_cache(self):
        for available, missing in ((False, []), (True, ['XY2/111'])):
            with tempfile.TemporaryDirectory() as tmp, \
                    patch('sys.argv', ['installer', '--source', tmp, '--premium-xy-only']), \
                    patch.object(installer, 'import_premium_xy_foils', return_value={
                        'written': 0, 'missing': missing, 'available': available}):
                self.assertEqual(installer.main(), 2)


if __name__ == '__main__':
    unittest.main()
