import unittest

from spirit.tools.import_hgss_sets import (
    HGSS_SETS,
    collector_number_text,
    energy_profile,
    internal_number,
)


class ImportHgssTests(unittest.TestCase):
    def test_complete_era_mapping(self):
        self.assertEqual(
            list(HGSS_SETS.values()),
            ["Promo_HGSS", "HGSS1", "HGSS2", "HGSS3", "HGSS4", "COL"],
        )

    def test_special_numbers_use_unique_internal_slots(self):
        self.assertEqual(internal_number({"number": "HGSS01"}, "hsp"), 1)
        self.assertEqual(internal_number({"number": "ONE"}, "hgss1"), 124)
        self.assertEqual(internal_number({"number": "THREE"}, "hgss3"), 91)
        self.assertEqual(internal_number({"number": "SL11"}, "col1"), 106)

    def test_printed_collector_label_is_preserved(self):
        self.assertEqual(collector_number_text({"number": "SL4"}), "SL4")
        self.assertIsNone(collector_number_text({"number": "42"}))

    def test_energy_profiles(self):
        dce = energy_profile({"name": "Double Colorless Energy", "subtypes": ["Special"]})
        self.assertEqual(dce["provides"], ["any:Colorless,Colorless"])
        rainbow = energy_profile({"name": "Rainbow Energy", "subtypes": ["Special"]})
        self.assertIn("Lightning", rainbow["providesAnyOf"])
        rescue = energy_profile({"name": "Rescue Energy", "subtypes": ["Special"]})
        self.assertEqual(rescue["provides"], ["Colorless"])


if __name__ == "__main__":
    unittest.main()
