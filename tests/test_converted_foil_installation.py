"""Converted foil packs install durable sources, without a Live importer."""
import tempfile
import unittest
import zipfile
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import patch

from PIL import Image
from spirit.tools import install_converted_foils as installer
from spirit.tools import import_foil_masks as masks


class ConvertedFoilInstallationTests(unittest.TestCase):
    def pack(self, root, codes=('PGO',)):
        for code in codes:
            for kind in installer.REQUIRED_KINDS:
                target = root / f'en_US_{code}_wp_{kind}_Foil2' / ('0' * 32) / '__data'
                target.parent.mkdir(parents=True)
                target.write_bytes(b'fixture')

    def test_all_four_collections_and_layers_are_checked_before_writing(self):
        with tempfile.TemporaryDirectory() as tmp, patch.object(masks, 'extract_set') as extract:
            root = Path(tmp)
            self.pack(root, ('PGO', 'SWSH11', 'SWSH12'))
            with self.assertRaisesRegex(ValueError, 'CZ'):
                installer.install(root)
            extract.assert_not_called()

    def test_complete_directory_installs_every_selected_set(self):
        with tempfile.TemporaryDirectory() as tmp, patch.object(masks, 'extract_set', return_value=(3, 0)) as extract:
            root = Path(tmp)
            self.pack(root, installer.SETS)
            self.assertEqual(installer.install(root), 12)
            self.assertEqual(extract.call_count, 4)
            for code, call in zip(installer.SETS, extract.call_args_list):
                self.assertEqual(call.args, (code, [str(root.resolve())]))
                self.assertEqual(call.kwargs, {'force': True, 'strict': True, 'container_only': True})

    def test_zip_with_wrapper_folder_is_supported(self):
        with tempfile.TemporaryDirectory() as tmp, patch.object(masks, 'extract_set', return_value=(3, 0)):
            archive = Path(tmp) / 'pack.zip'
            with zipfile.ZipFile(archive, 'w') as z:
                for kind in installer.REQUIRED_KINDS:
                    z.writestr(f'PGO-CRZLiveBundles/en_US_PGO_wp_{kind}_Foil2/{"0" * 32}/__data', b'fixture')
            self.assertEqual(installer.install(archive, ('PGO',)), 3)

    def test_invalid_source_and_unsupported_set_are_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            for source, sets in ((Path(tmp) / 'missing', ('PGO',)), (Path(tmp), ('SV1',))):
                with self.assertRaises(ValueError):
                    installer.install(source, sets)

    def test_decode_failure_is_reported_as_failure(self):
        with tempfile.TemporaryDirectory() as tmp:
            self.pack(Path(tmp))
            with patch('sys.argv', ['installer', '--source', tmp, '--sets', 'PGO']), \
                    patch.object(masks, 'extract_set', side_effect=ValueError('corrupt bundle')):
                self.assertEqual(installer.main(), 2)

    def test_empty_extraction_is_not_success(self):
        with tempfile.TemporaryDirectory() as tmp, patch.object(masks, 'extract_set', return_value=(0, 0)):
            self.pack(Path(tmp))
            with self.assertRaisesRegex(ValueError, 'no masks'):
                installer.install(Path(tmp), ('PGO',))

    def test_all_layers_preserve_pixels_and_card_face(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            self.pack(root)
            scripts = root / 'scripts' / 'PGO'
            scripts.mkdir(parents=True)
            (scripts / 'Charizard_10.py').write_text('collector_number=10')
            (scripts / 'Unused_20.py').write_text('collector_number=20')
            assets = root / 'cards' / 'PGO'
            assets.mkdir(parents=True)
            face = assets / 'Charizard_10.png'
            face.write_bytes(b'unchanged card face')
            source = Image.new('RGBA', (8, 8), (24, 80, 123, 64))
            data = SimpleNamespace(m_Name='010', image=source)
            texture = SimpleNamespace(type=SimpleNamespace(name='Texture2D'), read=lambda: data,
                                      file_id=0, path_id=1)
            unused = SimpleNamespace(type=SimpleNamespace(name='Texture2D'),
                                     read=lambda: SimpleNamespace(m_Name='020', image=source))
            with patch.object(masks, 'SCRIPTS_DIR', str(root / 'scripts')), \
                    patch.object(masks, 'CARDS_IMG_DIR', str(root / 'cards')), \
                    patch('UnityPy.load', return_value=SimpleNamespace(
                        objects=[texture, unused], container={'010': texture, 'PGO/010': texture})):
                self.assertEqual(installer.install(root, ('PGO',)), 3)
                self.assertEqual(installer.install(root, ('PGO',)), 3)
            for suffix in ('_foil', '_foil_ph', '_foil_secondary'):
                with Image.open(assets / f'Charizard_10{suffix}.png') as installed:
                    self.assertEqual(installed.tobytes(), source.tobytes())
            self.assertEqual(face.read_bytes(), b'unchanged card face')
            self.assertFalse(list(assets.glob('Unused*')))

    def test_strict_import_rejects_corrupt_or_unmatched_bundles(self):
        payload = SimpleNamespace(load_arg=lambda: b'broken', label='broken')
        with patch.object(masks, '_set_card_stems', return_value={'001': 'Card_1'}), \
                patch.object(masks, '_bundle_payloads', return_value=[payload]):
            with patch('UnityPy.load', side_effect=ValueError('invalid')):
                with self.assertRaisesRegex(ValueError, 'Cannot read'):
                    masks.extract_set('PGO', ['source'], strict=True)
            with patch('UnityPy.load', return_value=SimpleNamespace(objects=[])):
                with self.assertRaisesRegex(ValueError, 'no matching'):
                    masks.extract_set('PGO', ['source'], strict=True)


if __name__ == '__main__':
    unittest.main()
