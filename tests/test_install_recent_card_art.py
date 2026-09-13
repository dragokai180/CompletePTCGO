import unittest
import tempfile
from unittest.mock import patch
from pathlib import Path

from spirit.tools.install_recent_card_art import (
    RECENT_SETS,
    SCRIPTS_ROOT,
    build_tasks,
    load_image_urls,
    collector_number_from_script,
    image_url,
    mega_promo_url,
    selected_sets,
    install_native_energy,
    run,
)


class InstallRecentCardArtTests(unittest.TestCase):
    def test_swsh_energy_selected_by_default_and_code(self):
        self.assertIn("SWSH_Energy", {s.set_code for s in selected_sets([])})
        self.assertEqual(selected_sets(["SWSH_Energy"]),
                         [RECENT_SETS["swsh_energy"]])

    def test_swsh_energy_imports_all_native_prints_without_network(self):
        with tempfile.TemporaryDirectory() as directory:
            with patch("spirit.tools.install_recent_card_art.ASSETS_ROOT", Path(directory)), \
                 patch("spirit.tools.ptcgo_local_assets.install_card_art", return_value=True) as restore, \
                 patch("spirit.tools.install_recent_card_art.download_one") as download:
                run(["SWSH_Energy"], 1, False, "cbrew-fixture")
                self.assertEqual(restore.call_count, 17)
                self.assertEqual({c.args[1] for c in restore.call_args_list},
                                 {str(n) for n in range(1, 18)})
                self.assertTrue(all(c.kwargs["source"] == "cbrew-fixture"
                                    for c in restore.call_args_list))
                download.assert_not_called()

    def test_swsh_energy_preserves_existing_art(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            for script in (SCRIPTS_ROOT / "SWSH_Energy").glob("*.py"):
                destination = root / "SWSH_Energy" / (script.stem + ".png")
                destination.parent.mkdir(exist_ok=True)
                destination.write_bytes(b"original artwork")
            with patch("spirit.tools.install_recent_card_art.ASSETS_ROOT", root), \
                 patch("spirit.tools.ptcgo_local_assets.install_card_art", return_value=True) as restore:
                self.assertEqual(install_native_energy(False), [])
                restore.assert_not_called()
                self.assertEqual(install_native_energy(True), [])
                self.assertEqual(restore.call_count, 17)

    def test_swsh_energy_missing_cache_is_reported_as_failure(self):
        with tempfile.TemporaryDirectory() as directory:
            with patch("spirit.tools.install_recent_card_art.ASSETS_ROOT", Path(directory)), \
                 patch("spirit.tools.ptcgo_local_assets.install_card_art", return_value=False), \
                 patch("spirit.tools.install_recent_card_art.download_one") as download:
                with self.assertRaises(SystemExit) as raised:
                    run(["SWSH_Energy"], 1, False, "missing-cache")
                self.assertEqual(raised.exception.code, 2)
                download.assert_not_called()

    def test_default_includes_older_sets(self):
        codes = {s.set_code for s in selected_sets([])}
        self.assertTrue({"HGSS1", "BW6", "BW11", "Promo_XY", "HF"} <= codes)

    def test_all_old_scripts_have_catalog_urls(self):
        for card_set in selected_sets(["hgss", "bw", "xy", "sm"]):
            known = load_image_urls(card_set)
            for script in (SCRIPTS_ROOT / card_set.set_code).glob("*.py"):
                if script.name != "__init__.py":
                    with self.subTest(card=script.name, set=card_set.set_code):
                        self.assertIn(collector_number_from_script(script), known)

    def test_radiant_collection_and_promos_keep_printed_urls(self):
        self.assertIn("/bw11/RC17_hires.png", load_image_urls(RECENT_SETS["bw11"])["rc17"])
        self.assertIn("/bwp/BW48_hires.png", load_image_urls(RECENT_SETS["bwp"])["bw48"])

    def test_existing_bundle_art_is_preserved(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            scripts = root / "scripts" / "BW11"
            assets = root / "assets" / "BW11"
            scripts.mkdir(parents=True)
            assets.mkdir(parents=True)
            (scripts / "Audino_RC17.py").touch()
            (scripts / "Snivy_RC1.py").touch()
            existing = assets / "Snivy_RC1.png"
            existing.write_bytes(b"original cbrew artwork")
            with patch("spirit.tools.install_recent_card_art.SCRIPTS_ROOT", root / "scripts"), patch("spirit.tools.install_recent_card_art.ASSETS_ROOT", root / "assets"):
                tasks = build_tasks(RECENT_SETS["bw11"])
                self.assertEqual([path.name for _, path in tasks], ["Audino_RC17.png"])
                self.assertEqual(existing.read_bytes(), b"original cbrew artwork")
                self.assertEqual(len(build_tasks(RECENT_SETS["bw11"], overwrite=True)), 2)

    def test_sword_shield_era_contains_all_implemented_sets(self):
        selected = selected_sets(["sword-and-shield"])
        self.assertEqual(
            [card_set.set_code for card_set in selected],
            [
                "SWSH_Energy", "SWSH1", "SWSH2", "SWSH3", "SWSH35", "SWSH4",
                "SWSH45", "SWSH5", "SWSH6", "SWSH7", "CEL25",
                "SWSH8", "SWSH9", "SWSH10", "PGO", "SWSH11",
                "SWSH12", "CZ",
            ],
        )

    def test_mega_era_contains_main_sets_and_promos(self):
        selected = selected_sets(["mega"])
        self.assertEqual(
            [card_set.set_code for card_set in selected],
            ["ME1", "ME2", "ME2PT5", "ME3", "ME4", "ME5", "MEP"],
        )

    def test_script_filename_preserves_collector_number(self):
        self.assertEqual(
            collector_number_from_script(Path("AcerolasMischief_183.py")),
            "183",
        )

    def test_mega_promo_uses_english_limitless_archive(self):
        self.assertEqual(
            mega_promo_url("3"),
            "https://limitlesstcg.nyc3.cdn.digitaloceanspaces.com/"
            "tpci/MEP/MEP_003_R_EN.png",
        )

    def test_bundled_metadata_url_wins(self):
        card_set = RECENT_SETS["me2pt5"]
        self.assertEqual(
            image_url(card_set, "1", {"1": "https://example.test/card.png"}),
            "https://example.test/card.png",
        )

    def test_unknown_selection_is_rejected(self):
        with self.assertRaisesRegex(ValueError, "Unknown era or set"):
            selected_sets(["not-a-set"])


if __name__ == "__main__":
    unittest.main()
