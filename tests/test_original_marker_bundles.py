"""Gameplay marker bundles must retain the original atlas and public aliases."""
import gzip
import json
import os
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

import UnityPy
from spirit.server import auto_bundle_cosmetics as cosmetics
from spirit.server.manifest_manager import ManifestManager


class OriginalMarkerBundleTests(unittest.TestCase):
    def test_original_atlases_restore_custom_output_and_are_idempotent(self):
        with tempfile.TemporaryDirectory() as tmp:
            with patch.object(cosmetics, "BUNDLE_CACHE_DIR", tmp):
                for kind, folder in (("GX", "en_US_GXToken_CRR59_5"),
                                     ("VSTAR", "en_US_VSTARToken_CRR86_3")):
                    output = Path(tmp, folder, "00000000000000000000000001000000", "__data")
                    output.parent.mkdir(parents=True)
                    output.write_bytes(b"old custom atlas")
                    os.utime(output, (2000000000, 2000000000))
                    self.assertTrue(cosmetics.compile_original_marker_bundle(kind, folder))
                    template = Path(cosmetics.TEMPLATES_DIR, f"{kind}Token.template")
                    self.assertEqual(output.read_bytes(), template.read_bytes())
                    textures = [o.read().m_Name for o in UnityPy.load(output.read_bytes()).objects
                                if o.type.name == "Texture2D"]
                    self.assertEqual(textures, [f"{kind.lower()}tokentexture"])
                    before = output.stat().st_mtime_ns
                    self.assertTrue(cosmetics.compile_original_marker_bundle(kind, folder))
                    self.assertEqual(output.stat().st_mtime_ns, before)

    def test_manifest_exposes_native_marker_names_and_textures(self):
        with tempfile.TemporaryDirectory() as tmp:
            with patch.object(cosmetics, "BUNDLE_CACHE_DIR", tmp):
                cosmetics.compile_original_marker_bundle("GX", "en_US_GXToken_CRR59_5")
                cosmetics.compile_original_marker_bundle("VSTAR", "en_US_VSTARToken_CRR86_3")
            manager = ManifestManager([tmp])
            manifest = json.loads(gzip.decompress(manager.manifest_cache))
            for kind in ("GX", "VSTAR"):
                bundle = next(b for b in manifest["bundles"]
                              if b["name"].startswith(kind + "Token_CRR"))
                names = {a["name"] for a in bundle["assets"]}
                self.assertIn(kind + "Token", names)
                self.assertIn(f"{kind}Token/{kind.lower()}tokentexture", names)
                self.assertIn(kind.lower() + "tokentexture", names)
