import unittest

from spirit.packets.handlers.data_sync import _set_display_sort_key


class SetDisplayOrderTests(unittest.TestCase):
    def test_modern_series_are_above_archived_series(self):
        sets = [
            {"name": "BW1", "block": "BW", "number": 480},
            {"name": "SWSH1", "block": "SWSH", "number": 930},
            {"name": "SV2", "block": "SV", "number": 1130},
            {"name": "ME1", "block": "NONE", "number": 1260},
        ]

        self.assertEqual(
            [item["name"] for item in sorted(sets, key=_set_display_sort_key)],
            ["ME1", "SV2", "SWSH1", "BW1"],
        )

    def test_newest_expansion_is_first_inside_a_series(self):
        sets = [
            {"name": "ME1", "block": "NONE", "number": 1260},
            {"name": "ME3", "block": "NONE", "number": 1290},
            {"name": "ME2", "block": "NONE", "number": 1270},
        ]

        self.assertEqual(
            [item["name"] for item in sorted(sets, key=_set_display_sort_key)],
            ["ME3", "ME2", "ME1"],
        )


if __name__ == "__main__":
    unittest.main()
