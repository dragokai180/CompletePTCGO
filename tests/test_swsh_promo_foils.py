"""Native promo masks and permanent exclusion of tournament novelty prints."""
import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from spirit.game.excluded_prints import EXCLUDED_SWSH_PROMOS, excluded_print
from spirit.game.scripts.cards import ScriptLoader
from spirit.tools import import_foil_masks as masks
from spirit.tools import install_recent_card_art as downloader
from spirit.tools import ptcgo_local_assets as native
from spirit.tools import import_swsh_promos as catalog


class SwshPromoFoilsTests(unittest.TestCase):
    def test_excluded_numbers_exactly_match_printed_tournament_restriction(self):
        rows = json.loads((downloader.DATA_ROOT / 'swshp.json').read_text(encoding='utf-8'))
        expected = {int(row['number'][4:]) for row in rows if any(
            'cannot be used at official tournaments' in text.lower() for text in row.get('rules', []))}
        self.assertEqual(EXCLUDED_SWSH_PROMOS, expected)
        for number in expected:
            self.assertTrue(excluded_print('SWSHP', f'SWSH{number}'))
            self.assertFalse(excluded_print('SWSH1', number))
        self.assertFalse(excluded_print('Promo_SWSH', '287to290'))

    def test_removed_scripts_cannot_be_loaded_downloaded_or_masked_if_left_by_old_install(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            scripts = root / 'Promo_SWSH'
            scripts.mkdir()
            for number in EXCLUDED_SWSH_PROMOS:
                (scripts / f'Old_{number}.py').write_text('raise AssertionError("obsolete script executed")')
            instance = ScriptLoader(str(root))
            for path in scripts.iterdir():
                instance._load_script(str(path))
            self.assertEqual(instance.cards, [])
            with patch.object(downloader, 'SCRIPTS_ROOT', root), \
                    patch.object(downloader, 'ASSETS_ROOT', root / 'assets'), \
                    patch.object(downloader, 'load_image_urls', return_value={}):
                self.assertEqual(downloader.build_tasks(downloader.RECENT_SETS['swshp'], overwrite=True), [])
            with patch.object(masks, 'SCRIPTS_DIR', str(root)):
                self.assertEqual(masks._set_card_stems('Promo_SWSH'), {})
            with patch.object(native, '_cached_set_art') as cache:
                self.assertFalse(native.install_card_art('Promo_SWSH', 132, root / 'art.png'))
                cache.assert_not_called()

    def test_catalog_does_not_recreate_removed_promos(self):
        self.assertEqual(catalog.plan(), [])

    def test_native_masks_import_in_archive_order_with_strict_errors(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            for name in ('SM Cache.zip', 'BW Cache.zip'):
                (root / name).touch()
            with patch.object(masks, '_bundle_payloads', return_value=[]), \
                    patch.object(masks, 'extract_set', return_value=(224, 0)) as extract:
                result = native.import_swsh_promo_foils(root)
                self.assertEqual(result, {'written': 224, 'unchanged': 0, 'available': True})
                extract.assert_called_once_with('Promo_SWSH', [str(root / 'BW Cache.zip'),
                    str(root / 'SM Cache.zip')], force=True, strict=True)
            with patch.object(masks, '_bundle_payloads', return_value=[]), \
                    patch.object(masks, 'extract_set', side_effect=ValueError('corrupt bundle')):
                with self.assertRaisesRegex(ValueError, 'corrupt bundle'):
                    native.import_swsh_promo_foils(root)

    def test_absent_cache_does_not_generate_fallback_masks(self):
        with tempfile.TemporaryDirectory() as tmp, patch.object(masks, 'extract_set') as extract:
            self.assertFalse(native.import_swsh_promo_foils(Path(tmp))['available'])
            extract.assert_not_called()

    def test_extracted_cache_is_supported_and_applied_last(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            def payloads(directory, code, kind):
                return [object()] if directory == str(root / 'bundleCache') and kind == 'std' else []
            with patch.object(masks, '_bundle_payloads', side_effect=payloads), \
                    patch.object(masks, 'extract_set', return_value=(1, 0)) as extract:
                native.import_swsh_promo_foils(root)
                self.assertEqual(extract.call_args.args[1], [str(root / 'bundleCache')])
