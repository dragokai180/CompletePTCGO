import unittest
import io
import tempfile
from unittest.mock import patch, MagicMock
from pathlib import Path
from PIL import Image
import requests

from spirit.tools.install_recent_card_art import (
    RECENT_SETS,
    SCRIPTS_ROOT,
    build_tasks,
    load_image_urls,
    collector_number_from_script,
    image_url,
    image_candidates,
    download_one,
    mega_promo_url,
    selected_sets,
    install_native_energy,
    run,
)


class InstallRecentCardArtTests(unittest.TestCase):
    def test_sm_basic_energies_use_complete_limitless_scans(self):
        for number, code in zip(range(164, 173), 'GRWLPFDMY'):
            urls = image_candidates(RECENT_SETS['sm1'], str(number),
                                    {str(number): 'https://example.com/cropped.png'})
            self.assertEqual(urls, (
                'https://limitlesstcg.nyc3.cdn.digitaloceanspaces.com/'
                f'tpci/SUM/SUM_{code}_R_EN.png',))
        self.assertEqual(image_url(RECENT_SETS['sm1'], '163', {'163': 'secret'}), 'secret')

    def test_sm_energy_repairs_only_known_cropped_prints(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            scripts = root / 'scripts' / 'SM1'
            assets = root / 'assets' / 'SM1'
            scripts.mkdir(parents=True)
            assets.mkdir(parents=True)
            for name, size in [('GrassEnergy_164', (700, 990)),
                               ('FireEnergy_165', (736, 1024)),
                               ('WaterEnergy_166', (1024, 1024)),
                               ('MetalEnergy_163', (700, 990))]:
                (scripts / (name + '.py')).touch()
                Image.new('RGB', size).save(assets / (name + '.png'))
            with patch('spirit.tools.install_recent_card_art.SCRIPTS_ROOT', root / 'scripts'), \
                 patch('spirit.tools.install_recent_card_art.ASSETS_ROOT', root / 'assets'), \
                 patch('spirit.tools.install_recent_card_art.load_image_urls', return_value={}):
                tasks = build_tasks(RECENT_SETS['sm1'])
            self.assertEqual([p.name for _, p in tasks], ['GrassEnergy_164.png'])

    def test_swsh_energy_selected_by_default_and_code(self):
        self.assertIn("SWSH_Energy", {s.set_code for s in selected_sets([])})
        self.assertEqual(selected_sets(["SWSH_Energy"]),
                         [RECENT_SETS["swsh_energy"]])

    def test_swsh_energy_imports_all_native_prints_without_network(self):
        def restore_art(set_code, number, destination, **kwargs):
            destination.parent.mkdir(parents=True, exist_ok=True)
            destination.write_bytes(b"native fixture")
            return True
        with tempfile.TemporaryDirectory() as directory:
            with patch("spirit.tools.install_recent_card_art.ASSETS_ROOT", Path(directory)), \
                 patch("spirit.tools.ptcgo_local_assets.install_card_art", side_effect=restore_art) as restore, \
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

    def test_swsh_energy_missing_cache_falls_back_to_download(self):
        with tempfile.TemporaryDirectory() as directory:
            with patch("spirit.tools.install_recent_card_art.ASSETS_ROOT", Path(directory)), \
                 patch("spirit.tools.ptcgo_local_assets.install_card_art", return_value=False), \
                 patch("spirit.tools.install_recent_card_art.download_one",
                       return_value=(True, "downloaded")) as download:
                run(["SWSH_Energy"], 1, False, "missing-cache")
                self.assertEqual(download.call_count, 17)

    def test_swsh_download_needs_no_native_source(self):
        with tempfile.TemporaryDirectory() as directory:
            with patch("spirit.tools.install_recent_card_art.ASSETS_ROOT", Path(directory)), \
                 patch("spirit.tools.install_recent_card_art.install_native_energy") as native, \
                 patch("spirit.tools.install_recent_card_art.download_one",
                       return_value=(True, "downloaded")) as download:
                run(["swsh_energy"], 1, False)
                native.assert_not_called()
                self.assertEqual(download.call_count, 17)

    def test_all_implemented_directories_are_selected_by_default(self):
        selected = {s.set_code.casefold() for s in selected_sets([])}
        implemented = {
            p.name.casefold() for p in SCRIPTS_ROOT.iterdir()
            if p.is_dir() and any(p.glob("*.py"))
        }
        self.assertFalse(implemented - selected)

    def test_every_implemented_card_gets_a_download_task_on_clean_install(self):
        with tempfile.TemporaryDirectory() as directory:
            with patch("spirit.tools.install_recent_card_art.ASSETS_ROOT", Path(directory)):
                for entry in selected_sets([]):
                    scripts = [p for p in (SCRIPTS_ROOT / entry.set_code).glob("*.py")
                               if p.name != "__init__.py"]
                    tasks = build_tasks(entry)
                    self.assertEqual(len(tasks), len(scripts), entry.set_code)
                    self.assertTrue(all(urls for urls, _ in tasks))

    def test_new_promos_have_scrydex_and_limitless_alternatives(self):
        urls = image_candidates(RECENT_SETS["svp"], "219", {})
        self.assertIn("https://images.scrydex.com/pokemon/svp-219/large", urls)
        self.assertTrue(any("/SVP_219_R_EN.png" in url for url in urls))

    def test_scrydex_metadata_and_remapped_print_identity_are_preserved(self):
        urls = load_image_urls(RECENT_SETS["me3"])
        self.assertIn("images.scrydex.com", urls["1"])
        urls = image_candidates(RECENT_SETS["sm115"], "101",
                               {"101": "https://images.pokemontcg.io/sma/SV1_hires.png"})
        self.assertIn("https://images.scrydex.com/pokemon/sma-SV1/large", urls)
        self.assertFalse(any("sm115-101" in url for url in urls))

    def test_black_bolt_duplicate_number_does_not_replace_another_card(self):
        urls = load_image_urls(RECENT_SETS["zsv10pt5"])
        self.assertIn("/60_hires.png", urls["60"])
        self.assertIn("/80_hires.png", urls["80"])

    @staticmethod
    def image_response(format="PNG"):
        data = io.BytesIO()
        Image.new("RGB", (4, 6), "red").save(data, format=format)
        response = MagicMock()
        response.__enter__.return_value = response
        response.content = data.getvalue()
        return response

    def test_http_failure_tries_alternative_and_converts_jpeg(self):
        failed = MagicMock()
        failed.__enter__.return_value = failed
        failed.raise_for_status.side_effect = requests.HTTPError("404")
        with tempfile.TemporaryDirectory() as directory:
            destination = Path(directory) / "card.png"
            with patch("spirit.tools.install_recent_card_art.requests.get",
                       side_effect=[failed, self.image_response("JPEG")]) as get:
                ok, detail = download_one((("https://example.test/first",
                                           "https://example.test/second"), destination))
                self.assertTrue(ok, detail)
                self.assertEqual(get.call_count, 2)
                with Image.open(destination) as image:
                    self.assertEqual(image.format, "PNG")
                    self.assertEqual(image.size, (4, 6))

    def test_invalid_payload_preserves_existing_file_and_cleans_temporary_files(self):
        response = MagicMock()
        response.__enter__.return_value = response
        response.content = b"<html>Not an image</html>"
        with tempfile.TemporaryDirectory() as directory:
            destination = Path(directory) / "card.png"
            destination.write_bytes(b"existing")
            with patch("spirit.tools.install_recent_card_art.requests.get", return_value=response):
                ok, _ = download_one(("https://example.test/bad", destination))
            self.assertFalse(ok)
            self.assertEqual(destination.read_bytes(), b"existing")
            self.assertEqual(list(Path(directory).iterdir()), [destination])

    def test_download_failures_return_nonzero_exit(self):
        with tempfile.TemporaryDirectory() as directory:
            with patch("spirit.tools.install_recent_card_art.ASSETS_ROOT", Path(directory)), \
                 patch("spirit.tools.install_recent_card_art.download_one",
                       return_value=(False, "network unavailable")):
                with self.assertRaises(SystemExit) as raised:
                    run(["swsh_energy"], 1, False)
                self.assertEqual(raised.exception.code, 2)

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
                "SWSH_Energy", "Promo_SWSH", "SWSH1", "SWSH2", "SWSH3", "SWSH35", "SWSH4",
                "SWSH45", "SWSH5", "SWSH6", "SWSH7", "CEL25",
                "SWSH8", "SWSH9", "SWSH10", "PGO", "SWSH11",
                "SWSH12", "CZ",
            ],
        )

    def test_mega_era_contains_main_sets_and_promos(self):
        selected = selected_sets(["mega"])
        self.assertEqual(
            [card_set.set_code for card_set in selected],
            ["ME1", "ME2", "ME2PT5", "ME3", "ME4", "ME5", "ME55", "MEP"],
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
