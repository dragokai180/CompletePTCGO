import unittest
from unittest.mock import patch

from spirit.game.attributes import AttrID, DeckFormat
from spirit.game.data_utils import def_for
from spirit.game.format_manager import FormatManager, LEGACY_SETS
from spirit.game.models.formats import GameFormat
from spirit.game.rules import DeckValidator
from spirit.game.scripts.cards import loader


LEGACY = DeckFormat.LEGACY.value


class LegacyReprintTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        loader.load_all()

    def setUp(self):
        # Do not mutate the singleton used by other rule tests.
        self.manager = object.__new__(FormatManager)
        self.manager._initialized = False
        self.manager.__init__()

    @staticmethod
    def card(set_code, number):
        return next(c for c in loader.cards if c.key == set_code and
                    str(c.get_attribute_value(AttrID.COLLECTOR_NUMBER)) == str(number))

    def configure(self, **kwargs):
        fmt = GameFormat("Legacy", LEGACY, "Legacy", **kwargs)
        self.manager._by_guid[LEGACY] = fmt
        return fmt

    def test_trainers_and_special_energy_reprints(self):
        for set_code, number in (("CZ", 146), ("XY10", 105), ("SM1", 136)):
            with self.subTest(set=set_code, number=number):
                card = self.card(set_code, number)
                self.assertTrue(self.manager.is_card_eventually_legal(LEGACY, card))
                self.assertTrue(self.manager.is_card_legal(LEGACY, card))

    def test_equivalent_pokemon_with_modern_reminder_wording(self):
        for number in (31, 114):
            self.assertTrue(self.manager.is_card_legal(
                LEGACY, self.card("ZSV10PT5", number)))

    def test_same_name_different_attacks_is_not_a_reprint(self):
        for set_code, number in (("XY8", 61), ("CEL25", 10), ("SV3", 68)):
            with self.subTest(set=set_code, number=number):
                self.assertFalse(self.manager.is_card_legal(
                    LEGACY, self.card(set_code, number)))

    def test_new_trainers_and_special_energy_stay_illegal(self):
        for set_code, number in (("SWSH9", 151), ("XY2", 90)):
            self.assertFalse(self.manager.is_card_legal(
                LEGACY, self.card(set_code, number)))

    def test_legacy_original_remains_legal(self):
        self.assertTrue(self.manager.is_card_legal(LEGACY, self.card("BW4", 54)))

    def test_deck_validation_accepts_reprints_without_relaxing_copy_limit(self):
        pokemon = self.card("BW4", 54)
        trainer = self.card("CZ", 146)
        energy = next(c for c in loader.cards if c.key == "Free_Energy")
        cards = [pokemon.guid] + [trainer.guid] * 4 + [energy.guid] * 55
        validator = DeckValidator({"piles": {"deck": cards}})
        validator.manager = self.manager
        self.assertTrue(validator.validate([LEGACY])[0]["valid"])
        cards[5] = self.card("BW5", 102).guid
        validator = DeckValidator({"piles": {"deck": cards}})
        validator.manager = self.manager
        self.assertFalse(validator.validate([LEGACY])[0]["valid"])

    def test_changed_hp_or_ability_text_does_not_match(self):
        card = self.card("ZSV10PT5", 31)
        self.manager._legacy_reprints(self.manager.by_guid(LEGACY))
        definition = def_for(card.guid)
        ability = definition.abilities[0]
        with patch.object(ability, "game_text", "Attach 2 Lightning Energy cards."):
            self.assertFalse(self.manager.is_card_legal(LEGACY, card))
        original_get = card.get_attribute_value
        with patch.object(card, "get_attribute_value", side_effect=lambda attr:
                          100 if attr == AttrID.HP else original_get(attr)):
            self.assertFalse(self.manager.is_card_legal(LEGACY, card))

    def test_banned_reprint_stays_banned(self):
        self.configure(sets=["BW5"], banned_cards=["CZ/146"])
        self.assertFalse(self.manager.is_card_legal(LEGACY, self.card("CZ", 146)))

    def test_banned_source_cannot_legalize_reprint(self):
        self.configure(sets=["BW5"], banned_cards=["BW5/102"])
        self.assertFalse(self.manager.is_card_legal(LEGACY, self.card("CZ", 146)))

    def test_source_date_gate_applies_to_reprint(self):
        self.configure(sets=["BW5"], legal_from={"BW5": 2000})
        card = self.card("CZ", 146)
        self.assertTrue(self.manager.is_card_eventually_legal(LEGACY, card))
        self.assertFalse(self.manager.is_card_legal(LEGACY, card, now_ms=1999))
        self.assertTrue(self.manager.is_card_legal(LEGACY, card, now_ms=2000))

    def test_ban_changes_invalidate_cached_sources(self):
        fmt = self.configure(sets=["BW5"])
        card = self.card("CZ", 146)
        self.assertTrue(self.manager.is_card_legal(LEGACY, card))
        fmt.banned_cards.append("BW5/102")
        self.assertFalse(self.manager.is_card_legal(LEGACY, card))

    def test_expanded_accepts_equivalent_prints_too(self):
        guid = DeckFormat.EXPANDED.value
        self.manager._by_guid[guid] = GameFormat(
            "Expanded", guid, "Expanded", sets=["BW5"])
        self.assertTrue(self.manager.is_card_legal(guid, self.card("CZ", 146)))

    def test_hgss_expanded_reprints(self):
        guid = DeckFormat.EXPANDED.value
        for code, number in (
            ("COL", 77), ("HGSS1", 90), ("HGSS1", 103), ("HGSS1", 91),
            ("HGSS1", 92), ("HGSS1", 93), ("HGSS1", 94), ("HGSS1", 95),
            ("HGSS1", 96), ("HGSS1", 98), ("HGSS1", 104), ("HGSS1", 102),
            ("HGSS2", 78), ("HGSS2", 79), ("HGSS2", 80),
            ("HGSS2", 82), ("HGSS2", 83),
        ):
            with self.subTest(code=code, number=number):
                self.assertTrue(self.manager.is_card_legal(guid, self.card(code, number)))
        self.assertFalse(self.manager.is_card_legal(
            DeckFormat.STANDARD.value, self.card("HGSS1", 103)))
        self.assertFalse(self.manager.is_card_legal(guid, self.card("HGSS1", 108)))

    def test_expanded_reprint_respects_source_date_bans_and_copy_limit(self):
        guid = DeckFormat.EXPANDED.value
        fmt = GameFormat("Expanded", guid, "Expanded", sets=["BW4"],
                         legal_from={"BW4": 2000})
        self.manager._by_guid[guid] = fmt
        card = self.card("HGSS1", 103)
        self.assertFalse(self.manager.is_card_legal(guid, card, now_ms=1999))
        self.assertTrue(self.manager.is_card_legal(guid, card, now_ms=2000))
        fmt.banned_cards = ["HGSS1/103"]
        self.assertFalse(self.manager.is_card_legal(guid, card))
        fmt.banned_cards = ["BW4/92"]
        self.assertFalse(self.manager.is_card_legal(guid, card))
        fmt.banned_cards = []
        pokemon = self.card("BW4", 54)
        energy = next(c for c in loader.cards if c.key == "Free_Energy")
        cards = [pokemon.guid, card.guid] + [self.card("BW4", 92).guid] * 3 + [energy.guid] * 55
        validator = DeckValidator({"piles": {"deck": cards}})
        validator.manager = self.manager
        self.assertTrue(validator.validate([guid])[0]["valid"])
        cards[5] = card.guid
        validator = DeckValidator({"piles": {"deck": cards}})
        validator.manager = self.manager
        self.assertFalse(validator.validate([guid])[0]["valid"])

    def test_reprint_indexes_are_cached_per_format(self):
        legacy = self.manager.by_guid(LEGACY)
        expanded = self.manager.by_guid(DeckFormat.EXPANDED.value)
        old_index = self.manager._legacy_reprints(legacy)
        new_index = self.manager._legacy_reprints(expanded)
        self.assertIs(old_index, self.manager._legacy_reprints(legacy))
        self.assertIs(new_index, self.manager._legacy_reprints(expanded))

    def test_index_is_cached_and_rebuilt_after_catalog_replacement(self):
        fmt = self.manager.by_guid(LEGACY)
        index = self.manager._legacy_reprints(fmt)
        self.assertIs(index, self.manager._legacy_reprints(fmt))
        with patch.object(loader, "cards", list(loader.cards)):
            self.assertIsNot(index, self.manager._legacy_reprints(fmt))

    def test_configured_sets_still_limit_reprint_sources(self):
        fmt = self.configure(sets=["BW5"])
        card = self.card("CZ", 146)
        self.assertTrue(self.manager.is_card_legal(LEGACY, card))
        fmt.sets = ["BW1"]
        self.assertFalse(self.manager.is_card_legal(LEGACY, card))

    def test_fallback_contains_entire_legacy_era(self):
        self.assertTrue({"HGSS1", "COL", "BW1", "BW11", "PROMO_BW"} <= LEGACY_SETS)


if __name__ == "__main__":
    unittest.main()
