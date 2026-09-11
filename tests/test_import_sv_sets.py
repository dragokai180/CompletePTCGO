import unittest

from spirit.tools.import_sv_sets import SET_NAMES, SV_SETS, energy_profile


class ImportScarletVioletTests(unittest.TestCase):
    def test_complete_era_mapping_contains_the_four_previous_gaps(self):
        self.assertEqual(SV_SETS["sv3"][:2], ("SV3", "OBF"))
        self.assertEqual(SV_SETS["sv3pt5"][:2], ("SV035", "MEW"))
        self.assertEqual(SV_SETS["sv4"][:2], ("SV4", "PAR"))
        self.assertEqual(SV_SETS["sv4pt5"][:2], ("SV045", "PAF"))
        self.assertIn("SVE", SET_NAMES)
        self.assertIn("SVP", SET_NAMES)

    def test_energy_profile_reads_basic_type(self):
        profile = energy_profile({
            "name": "Basic Fire Energy", "subtypes": ["Basic"], "rules": []
        })
        self.assertEqual(profile["energyKind"], "basic")
        self.assertEqual(profile["provides"], ["Fire"])

    def test_energy_profile_exposes_every_type_special_energy(self):
        profile = energy_profile({
            "name": "Luminous Energy",
            "subtypes": ["Special"],
            "rules": ["This card provides every type of Energy."],
        })
        self.assertEqual(profile["energyKind"], "special")
        self.assertIn("Grass", profile["providesAnyOf"])
        self.assertIn("Metal", profile["providesAnyOf"])


if __name__ == "__main__":
    unittest.main()
