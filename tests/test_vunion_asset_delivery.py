"""The composed V-UNION face must be discoverable and downloadable in a match."""
import gzip
import io
import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

import UnityPy
from PIL import Image

from re_tools import create_card_bundle
from spirit.server.http_server import MockHTTPRequestHandler
from spirit.server.manifest_manager import ManifestManager
from spirit.server.bundle_variants import DiskBundleCache, trim_textures


class _CountingBuffer(io.BytesIO):
    def __init__(self):
        super().__init__()
        self.largest_write = 0

    def write(self, data):
        self.largest_write = max(self.largest_write, len(data))
        return super().write(data)


class VUnionAssetDeliveryTests(unittest.TestCase):
    def test_disk_cache_persists_variant_and_invalidates_changed_key(self):
        with tempfile.TemporaryDirectory() as tmp:
            first = DiskBundleCache(tmp, 1024)
            first.put('source:metal:v1', b'bundle bytes')
            second = DiskBundleCache(tmp, 1024)
            self.assertEqual(second.get('source:metal:v1'), b'bundle bytes')
            self.assertIsNone(second.get('source:metal:v2'))

    def test_type_trim_retains_combined_vunion_face(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            art = root / 'art.png'
            Image.new('RGBA', (32, 32), (25, 80, 140, 255)).save(art)
            template = Path(__file__).resolve().parents[1] / 'spirit/templates/card_bundle'
            with patch.object(create_card_bundle, 'OUTPUT_DIR', str(root)), \
                    patch.object(create_card_bundle, 'ASSET_MAP_PATH', str(root / 'unused-map.json')):
                create_card_bundle.create_card_set_bundle(
                    {'163to166': str(art), '164': str(art)}, str(template), 'en_US_Promo_SWSH')
            bundle_path = root / 'en_US_Promo_SWSH/00000000000000000000000001000000/__data'
            env = UnityPy.load(bundle_path.read_bytes())
            self.assertTrue(trim_textures(env, 'Promo_SWSH', 'metal', {164: {'fire'}}))
            env = UnityPy.load(env.file.save(packer='lz4'))
            bundle = next(obj for obj in env.objects if obj.type.name == 'AssetBundle').read()
            names = {name for name, _ in bundle.m_Container}
            self.assertIn('163to166', names)
            self.assertIn('to166', names)
            self.assertNotIn('164', names)

    def test_combined_texture_has_playmat_and_zoom_names(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            art = root / 'combined.png'
            Image.new('RGBA', (32, 32), (25, 80, 140, 255)).save(art)
            template = Path(__file__).resolve().parents[1] / 'spirit/templates/card_bundle'
            with patch.object(create_card_bundle, 'OUTPUT_DIR', str(root)), \
                    patch.object(create_card_bundle, 'ASSET_MAP_PATH', str(root / 'unused-map.json')):
                create_card_bundle.create_card_set_bundle(
                    {'163to166': str(art)}, str(template), 'en_US_Promo_SWSH')
            bundle_path = root / 'en_US_Promo_SWSH/00000000000000000000000001000000/__data'
            env = UnityPy.load(bundle_path.read_bytes())
            bundle = next(obj for obj in env.objects if obj.type.name == 'AssetBundle').read()
            entries = {name: int(info.asset.m_PathID) for name, info in bundle.m_Container}
            self.assertEqual(entries['163to166'], entries['to166'])
            self.assertEqual(entries['163to166'], entries['Promo_SWSH/to166'])
            self.assertEqual(entries['163to166'], entries['Promo_SWSH_to166'])

    def test_combined_face_is_listed_in_type_bundle(self):
        faces = ('139to142', '155to158', '159to162',
                 '163to166', '215to218', '287to290')
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp, 'en_US_Promo_SWSH', 'cab', '__data')
            path.parent.mkdir(parents=True)
            path.write_bytes(b'fixture bundle')
            manager = ManifestManager([tmp])
            manager.asset_map = {'en_US_Promo_SWSH': ['159', *faces]}
            manifest = json.loads(gzip.decompress(manager.generate_manifest(force_refresh=True)))

        bundles = {bundle['name']: bundle for bundle in manifest['bundles']}
        for name in ('Promo_SWSH', 'Promo_SWSH_psychic',
                     'Promo_SWSH_lightning', 'Promo_SWSH_metal'):
            names = {item['name'] for item in bundles[name]['assets']}
            for face in faces:
                self.assertIn(f'{name}/{face}', names)
                self.assertIn(f"{name}/to{face.split('to', 1)[1]}", names)
            expected_path = ('en_US/en_US_Promo_SWSH.unity3d' if name == 'Promo_SWSH'
                             else f'en_US/en_US_{name}.unity3d')
            self.assertEqual(bundles[name]['WebPath'], expected_path)

    def test_numbered_art_routes_by_type_without_losing_vunion(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp, 'en_US_Promo_SWSH', 'cab', '__data')
            path.parent.mkdir(parents=True)
            path.write_bytes(b'fixture bundle')
            manager = ManifestManager([tmp])
            manager.asset_map = {'en_US_Promo_SWSH': ['164', '163to166']}
            manager.card_partitions = {'Promo_SWSH': {164: {'fire'}}}
            manifest = json.loads(gzip.decompress(manager.generate_manifest(force_refresh=True)))
        bundles = {bundle['name']: {asset['name'] for asset in bundle['assets']}
                   for bundle in manifest['bundles']}
        self.assertIn('Promo_SWSH/164', bundles['Promo_SWSH_fire'])
        self.assertNotIn('Promo_SWSH/164', bundles['Promo_SWSH_metal'])
        self.assertNotIn('Promo_SWSH/164', bundles['Promo_SWSH'])
        self.assertIn('Promo_SWSH_metal/to166', bundles['Promo_SWSH_metal'])

    def test_physical_bundle_streams_and_supports_resume(self):
        payload = bytes(range(256)) * 3000
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp, 'bundle.unity3d')
            path.write_bytes(payload)
            for requested_range, expected_status, expected_body, expected_range in (
                (None, 200, payload, None),
                ('bytes=262144-262399', 206, payload[262144:262400],
                 f'bytes 262144-262399/{len(payload)}'),
                ('bytes=-64', 206, payload[-64:],
                 f'bytes {len(payload)-64}-{len(payload)-1}/{len(payload)}'),
            ):
                with self.subTest(range=requested_range):
                    handler = object.__new__(MockHTTPRequestHandler)
                    handler.headers = {'Range': requested_range} if requested_range else {}
                    handler.wfile = _CountingBuffer()
                    response = {}
                    headers = {}
                    handler.send_response = lambda status: response.setdefault('status', status)
                    handler.send_header = lambda key, value: headers.setdefault(key, value)
                    handler.end_headers = lambda: None
                    handler._send_bundle_file(str(path))
                    self.assertEqual(response['status'], expected_status)
                    self.assertEqual(handler.wfile.getvalue(), expected_body)
                    self.assertEqual(headers.get('Content-Range'), expected_range)
                    self.assertLessEqual(handler.wfile.largest_write, 256 * 1024)


if __name__ == '__main__':
    unittest.main()
