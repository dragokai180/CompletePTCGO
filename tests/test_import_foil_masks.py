import os
import tempfile
import unittest
import zipfile
from unittest.mock import patch

from spirit.tools import import_foil_masks


class ImportFoilMasksTests(unittest.TestCase):
    def test_zip_payloads_find_only_requested_set_and_kind(self):
        with tempfile.TemporaryDirectory() as tmp:
            cache = os.path.join(tmp, "cache.zip")
            with zipfile.ZipFile(cache, "w") as archive:
                archive.writestr(
                    "root/bundleCache/en_US_BW10_wp_std_Foil2_CR1/"
                    "00000000000000000000000001000000/__data",
                    b"standard",
                )
                archive.writestr(
                    "root/bundleCache/en_US_BW10_wp_ph_Foil2_CR1/"
                    "00000000000000000000000001000000/__data",
                    b"parallel",
                )
                archive.writestr(
                    "root/bundleCache/en_US_SM8_wp_std_Foil2_CR1/"
                    "00000000000000000000000001000000/__data",
                    b"other set",
                )

            payloads = import_foil_masks._zip_payloads(cache, "BW10", "std")

            self.assertEqual(len(payloads), 1)
            self.assertEqual(payloads[0].load_arg(), b"standard")

    def test_directory_payloads_accept_unsuffixed_bundle(self):
        with tempfile.TemporaryDirectory() as tmp:
            data_dir = os.path.join(
                tmp,
                "en_US_BW10_wp_std_Foil2",
                "00000000000000000000000001000000",
            )
            os.makedirs(data_dir)
            data_path = os.path.join(data_dir, "__data")
            with open(data_path, "wb") as bundle:
                bundle.write(b"bundle")

            payloads = import_foil_masks._directory_payloads(tmp, "BW10", "std")

            self.assertEqual([item.path for item in payloads], [data_path])

    def test_collector_texture_number_rejects_alternate_print_names(self):
        self.assertEqual(import_foil_masks._collector_texture_number("7"), "007")
        self.assertEqual(import_foil_masks._collector_texture_number("007"), "007")
        self.assertIsNone(import_foil_masks._collector_texture_number("007xy"))
        self.assertIsNone(import_foil_masks._collector_texture_number("foil_007"))

    def test_cache_set_alias_precedes_exact_repository_code(self):
        self.assertEqual(
            import_foil_masks._cache_set_codes("SWSH35"),
            ("CP", "SWSH35"),
        )
        self.assertEqual(
            import_foil_masks._cache_set_codes("BW10"),
            ("BW10",),
        )


if __name__ == "__main__":
    unittest.main()
