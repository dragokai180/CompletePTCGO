import json
import unittest
from unittest.mock import patch

from spirit.game import data_utils
from spirit.game.attributes import AttrID, FoilEffects, FoilMasks, Rarities
from spirit.tools.sync_foil_metadata import _compact_record


class FoilMetadataTests(unittest.TestCase):
    def test_crown_zenith_signed_bede_is_an_illustration_holo(self):
        known, foil = data_utils._print_foil('CZ', 124, Rarities.RareHolo, ['Supporter'])
        self.assertTrue(known)
        self.assertIsNotNone(foil)
        self.assertEqual(foil.style, 'window')
        self.assertEqual(foil.effects, [FoilEffects.SWHOLO])

    def test_compact_record_retains_secondary_effect_order(self):
        record = _compact_record({
            "200610": "SwSecret",
            "200611": ["FlatSilver"],
            "200620": "Etched",
            "201000": True,
            "202080": 201,
        })

        self.assertEqual(record["effect"], "SwSecret")
        self.assertEqual(record["effects"], ["FlatSilver"])

    def test_print_foil_emits_primary_and_secondary_client_attributes(self):
        record = {
            "effect": "SwSecret",
            "effects": ["FlatSilver"],
            "mask": "Etched",
            "intensity": 201,
            "full_art": True,
        }
        with patch.dict(data_utils._PRINT_FOIL_METADATA, {"TEST": {"1": record}}):
            known, foil = data_utils._print_foil(
                "TEST", 1, Rarities.RareSecret, []
            )

        self.assertTrue(known)
        self.assertEqual(foil.mask, FoilMasks.ETCHED)
        self.assertEqual(
            foil.effects,
            [FoilEffects.SWSECRET, FoilEffects.FLATSILVER],
        )
        attrs = foil.to_attributes()
        self.assertEqual(
            json.loads(attrs[str(AttrID.FOIL_EFFECTS.value)]["value"]),
            [FoilEffects.FLATSILVER.value],
        )

    def test_brilliant_stars_mewtwo_is_not_a_primary_foil(self):
        known, foil = data_utils._print_foil(
            "SWSH9", 56, Rarities.Rare, ["Basic"]
        )

        self.assertTrue(known)
        self.assertIsNone(foil)

    def test_pokemon_go_pikachu_27_is_only_reverse_foil(self):
        known, foil = data_utils._print_foil(
            "PGO", 27, Rarities.Rare, ["Basic"]
        )

        self.assertTrue(known)
        self.assertIsNone(foil)

    def test_boundaries_crossed_ace_specs_keep_their_primary_foil(self):
        for collector_number in range(137, 141):
            with self.subTest(collector_number=collector_number):
                known, foil = data_utils._print_foil(
                    "BW7", collector_number, Rarities.Ace, ["ACE SPEC"]
                )

                self.assertTrue(known)
                self.assertIsNotNone(foil)
                self.assertEqual(foil.mask, FoilMasks.REVERSE)
                self.assertEqual(foil.effects, [FoilEffects.RAINBOW])

    def test_every_dragon_vault_print_is_foil(self):
        for collector_number in range(1, 22):
            with self.subTest(collector_number=collector_number):
                known, foil = data_utils._print_foil(
                    "DV", collector_number, Rarities.RareHolo, []
                )

                self.assertTrue(known)
                self.assertIsNotNone(foil)

    def test_unknown_print_does_not_receive_a_rarity_fallback(self):
        with patch.dict(data_utils._PRINT_FOIL_METADATA, {}, clear=True):
            card = data_utils.CardDefinition(
                guid="00000000-0000-0000-0000-00000000f011",
                key="TEST",
                name="test.foil.name",
                collector_number=1,
                set_code="TEST",
                rarity=Rarities.RareHolo,
            )

        self.assertIsNone(card.foil)
        self.assertNotIn(str(AttrID.FOIL_EFFECT.value), card.extra_attributes)


if __name__ == "__main__":
    unittest.main()
