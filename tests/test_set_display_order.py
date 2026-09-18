import unittest
import json
from pathlib import Path

from spirit.packets.handlers.data_sync import _set_display_sort_key


class SetDisplayOrderTests(unittest.TestCase):
    def test_mega_energy_is_last_regular_set_before_promos_in_native_client(self):
        root = Path(__file__).resolve().parents[1]
        sets = json.loads((root / "spirit/database/json_data/sets.json").read_text())
        mega = [row for row in sets if row.get("filter") and row.get("block") == "NONE"]
        expected = ["ME55", "ME5", "ME4", "ME3", "ME2PT5", "ME2", "ME1", "MEE", "MEP"]
        # ExpansionCollapsibleDataSource orders non-Trainer-Kit rows by promo
        # first, then descending number. Server-only numeric adjacency is not
        # enough: a promo's number does not determine its visible position.
        native_order = sorted(mega, key=lambda row: (bool(row.get("promo")), -row["number"]))
        self.assertEqual([row["name"] for row in native_order], expected)
        self.assertEqual([row["name"] for row in sorted(mega, key=_set_display_sort_key)], expected)

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
