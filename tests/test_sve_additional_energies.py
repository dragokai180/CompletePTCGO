"""SVE 017-024 are distinct Basic prints without enabled foil."""
import importlib
import json
import unittest
from pathlib import Path

from spirit.game.attributes import AttrID


class AdditionalSveEnergyTests(unittest.TestCase):
    def test_all_printings_have_distinct_identity_and_basic_rules(self):
        guids = set()
        kinds = ("Grass", "Fire", "Water", "Lightning", "Psychic", "Fighting", "Darkness", "Metal")
        for number in range(1, 25):
            kind = kinds[(number - 1) % 8]
            card = importlib.import_module(
                f"spirit.game.scripts.cards.SVE.Basic{kind}Energy_{number}").card
            attrs = card.to_archetype_dict()["attributes"]
            with self.subTest(number=number):
                self.assertEqual(card.set_code, "SVE")
                self.assertEqual(card.collector_number, number)
                self.assertIn("Basic", card.subtypes)
                self.assertFalse(attrs.get(str(AttrID.IS_SPECIAL_ENERGY.value), {}).get("value", False))
                self.assertEqual(json.loads(attrs[str(AttrID.ENERGY_INFO.value)]["value"]),
                                 {"options": [[card.energy_type.value]]})
                self.assertEqual(attrs[str(AttrID.IMAGE_URL.value)]["value"], f"{number:03}")
                self.assertIsNone(card.foil)
                self.assertNotIn(card.guid, guids)
                guids.add(card.guid)
        self.assertEqual(len(guids), 24)

    def test_catalog_count_includes_new_printings(self):
        root = Path(__file__).resolve().parents[1]
        sets = json.loads((root / "spirit/database/json_data/sets.json").read_text())
        self.assertEqual(next(row["count"] for row in sets if row["name"] == "SVE"), 24)
