import unittest
from pathlib import Path

import UnityPy

from re_tools.bundle_integrity import ensure_asset_bundle, repair_serialized_file_size


class BundleIntegrityTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.template = Path(__file__).resolve().parents[1] / (
            'spirit/templates/card_bundle/00000000000000000000000001000000/__data')

    def test_valid_bundle_is_unchanged(self):
        data = self.template.read_bytes()
        self.assertIs(ensure_asset_bundle(data), data)

    def test_two_byte_inner_size_mismatch_is_repaired(self):
        env = UnityPy.load(self.template.read_bytes())
        raw = bytearray(next(iter(env.file.files.values())).save())
        raw[4:8] = (len(raw) + 2).to_bytes(4, 'big')
        fixed = repair_serialized_file_size(raw)
        self.assertEqual(int.from_bytes(fixed[4:8], 'big'), len(fixed))
        self.assertTrue(UnityPy.load(fixed).objects)

    def test_unreadable_texture_is_rejected(self):
        env = UnityPy.load(self.template.read_bytes())
        texture = next(obj for obj in env.objects if obj.type.name == 'Texture2D')
        raw = bytearray(texture.get_raw_data())
        raw[:4] = (0x7fffffff).to_bytes(4, 'little')
        texture.set_raw_data(bytes(raw))
        with self.assertRaisesRegex(ValueError, 'unreadable Texture2D'):
            ensure_asset_bundle(env.file.save(packer='lz4'))


if __name__ == '__main__':
    unittest.main()
