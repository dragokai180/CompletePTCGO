"""The anniversary Energy printings keep their own artwork and Basic rules."""
import importlib
import json
import unittest
from pathlib import Path

from spirit.game.attributes import AttrID, PokemonTypes
from spirit.game.localization_overrides import SET_NAME_LOCALIZATION_OVERRIDES


class AnniversaryEnergyTests(unittest.TestCase):
    def test_all_sixteen_printings_keep_basic_energy_rules_and_unique_identity(self):
        kinds = ("Grass", "Fire", "Water", "Lightning", "Psychic", "Fighting", "Darkness", "Metal")
        guids = set()
        for number in range(1, 17):
            base_number = (number - 1) % 8 + 1
            kind = kinds[base_number - 1]
            card = importlib.import_module(
                f"spirit.game.scripts.cards.MEE.Basic{kind}Energy_{number}").card
            base = importlib.import_module(
                f"spirit.game.scripts.cards.SVE.Basic{kind}Energy_{base_number}").card
            with self.subTest(number=number, kind=kind):
                attrs = card.to_archetype_dict()["attributes"]
                self.assertFalse(attrs.get(str(AttrID.IS_SPECIAL_ENERGY.value), {}).get("value", False))
                self.assertEqual(card.energy_type, getattr(PokemonTypes, kind.upper()))
                self.assertEqual(json.loads(attrs[str(AttrID.ENERGY_INFO.value)]["value"]),
                                 {"options": [[card.energy_type.value]]})
                self.assertIn("Basic", card.subtypes)
                self.assertEqual(card.set_code, "MEE")
                self.assertEqual(base.set_code, "SVE")
                self.assertNotEqual(card.guid, base.guid)
                self.assertEqual(attrs[str(AttrID.IMAGE_URL.value)]["value"], f"{number:03}")
                guids.add(card.guid)
        self.assertEqual(len(guids), 16)

    def test_set_is_registered_separately_from_thirtieth_celebration(self):
        root = Path(__file__).resolve().parents[1]
        sets = json.loads((root / "spirit/database/json_data/sets.json").read_text())
        mee = [row for row in sets if row["name"] == "MEE"]
        self.assertEqual(len(mee), 1)
        self.assertTrue(mee[0]["filter"])
        self.assertEqual(mee[0]["block"], "NONE")
        from spirit.packets.handlers.data_sync import _set_display_sort_key
        order = [row["name"] for row in sorted(
            (row for row in sets if row["block"] == "NONE" and row.get("filter")),
            key=_set_display_sort_key)]
        self.assertEqual(order[order.index("MEE") + 1], "MEP")
        self.assertEqual(order[order.index("MEE") - 1], "ME1")
        self.assertEqual(mee[0]["count"], 16)
        self.assertIn("set.name.mee", SET_NAME_LOCALIZATION_OVERRIDES)
        formats = json.loads((root / "spirit/database/json_data/formats.json").read_text())
        for fmt in formats["formats"]:
            if "SVE" in fmt["sets"]:
                self.assertEqual(fmt["sets"].count("MEE"), 1)
