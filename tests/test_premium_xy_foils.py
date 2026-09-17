"""Premium XY promos use native variant masks, never regular-art copies."""
import tempfile
import unittest
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import patch

from PIL import Image
from spirit.game.foil_corrections import apply_foil_corrections
from spirit.game.foil_variants import PREMIUM_XY_FOIL_VARIANTS
from spirit.tools import import_foil_masks as importer


class PremiumXYFoilTests(unittest.TestCase):
    def test_all_fourteen_prints_have_exact_variant_identities(self):
        self.assertEqual(sum(map(len, PREMIUM_XY_FOIL_VARIANTS.values())), 14)
        for code, variants in PREMIUM_XY_FOIL_VARIANTS.items():
            with self.subTest(code=code):
                aliases = importer._variant_aliases(code)
                for internal, native in variants.items():
                    self.assertEqual(aliases[native], internal.zfill(3))
                    self.assertNotIn(internal, importer.INTERNAL_FOIL_ALIASES.get(code, {}))
        self.assertEqual(importer._variant_aliases('XY9')['098xy'], '128')
        self.assertNotEqual(importer._variant_aliases('XY9').get('098ya'), '128')

    def test_materials_replace_stale_regular_metadata_without_changing_base(self):
        original = {'effect': 'Tinsel', 'mask': 'Reverse', 'intensity': 150}
        metadata = {code: {slot: dict(original) for slot in variants}
                    for code, variants in PREMIUM_XY_FOIL_VARIANTS.items()}
        metadata['XY2']['88'] = dict(original)
        apply_foil_corrections(metadata)
        self.assertEqual(metadata['XY2']['88'], original)
        for code, variants in PREMIUM_XY_FOIL_VARIANTS.items():
            for slot in variants:
                record = metadata[code][slot]
                self.assertEqual(record['effect'], 'Rainbow')
                self.assertTrue(record['full_art'])
                self.assertEqual(record['mask'], 'Holo' if (code, slot) == ('PROMO_XY', '212') else 'Etched')

    def texture(self, name, color):
        data = SimpleNamespace(m_Name=name, image=Image.new('RGBA', (4, 4), color))
        return SimpleNamespace(type=SimpleNamespace(name='Texture2D'), read=lambda: data)

    def extract(self, root, with_variant=True):
        scripts = root / 'scripts' / 'XY2'
        assets = root / 'assets' / 'XY2'
        scripts.mkdir(parents=True)
        assets.mkdir(parents=True)
        (scripts / 'Blacksmith_88.py').write_text('collector_number=88')
        (scripts / 'Blacksmith_111.py').write_text('collector_number=111')
        for name in ('Blacksmith_111_foil.png', 'Blacksmith_111_foil_ph.png', 'Blacksmith_88_foil.png'):
            Image.new('RGBA', (4, 4), 'red').save(assets / name)
        objects = [self.texture('088', 'red')]
        if with_variant:
            objects.append(self.texture('088xy', 'blue'))
        # Unrelated native numeric slots must not overwrite the exact variant.
        objects.append(self.texture('111', 'red'))
        payload = SimpleNamespace(load_arg=lambda: b'bundle', label='test-native')
        with patch.object(importer, 'SCRIPTS_DIR', str(root / 'scripts')), \
                patch.object(importer, 'CARDS_IMG_DIR', str(root / 'assets')), \
                patch.object(importer, '_bundle_payloads', side_effect=lambda src, code, kind: [payload] if kind == 'std' else []), \
                patch('UnityPy.load', return_value=SimpleNamespace(objects=objects)):
            importer.extract_set('XY2', ['source'], force=True, only_cards=['111'])
        return assets

    def test_imports_variant_and_removes_stale_regular_reverse_mask(self):
        with tempfile.TemporaryDirectory() as tmp:
            assets = self.extract(Path(tmp))
            with Image.open(assets / 'Blacksmith_111_foil.png') as image:
                self.assertEqual(image.getpixel((0, 0)), (0, 0, 255, 255))
            self.assertFalse((assets / 'Blacksmith_111_foil_ph.png').exists())
            self.assertTrue((assets / 'Blacksmith_88_foil.png').exists())

    def test_absent_variant_does_not_fall_back_to_regular_mask(self):
        with tempfile.TemporaryDirectory() as tmp:
            assets = self.extract(Path(tmp), with_variant=False)
            self.assertFalse((assets / 'Blacksmith_111_foil.png').exists())
            self.assertFalse((assets / 'Blacksmith_111_foil_ph.png').exists())
            self.assertTrue((assets / 'Blacksmith_88_foil.png').exists())
