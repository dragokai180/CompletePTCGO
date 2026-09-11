import unittest

from spirit.database.player_data import (
    BASIC_ENERGY_GRANT_COUNT,
    _all_cards_grant_count,
)
from spirit.game.attributes import AttrID, CardType


class _Card:
    def __init__(self, card_type, *, special_energy=False, subtypes=None):
        self.card_type = card_type
        self.special_energy = special_energy
        self.subtypes = subtypes or []

    def get_attribute_value(self, attribute_id):
        if attribute_id == AttrID.CARD_TYPE:
            return self.card_type
        if attribute_id == AttrID.IS_SPECIAL_ENERGY:
            return self.special_energy
        return None


class GrantAllCardsQuantityTests(unittest.TestCase):
    def test_basic_energy_gets_59_copies(self):
        card = _Card(CardType.ENERGY.value, subtypes=["Basic"])
        self.assertEqual(BASIC_ENERGY_GRANT_COUNT, 59)
        self.assertEqual(_all_cards_grant_count(card), 59)

    def test_special_energy_remains_a_regular_four_copy_card(self):
        card = _Card(
            CardType.ENERGY.value,
            special_energy=True,
            subtypes=["Special"],
        )
        self.assertEqual(_all_cards_grant_count(card), 4)

    def test_every_one_copy_subtype_gets_one_copy(self):
        for subtype in ("ACE SPEC", "Prism Star", "Radiant", "V-UNION"):
            with self.subTest(subtype=subtype):
                card = _Card(CardType.POKEMON.value, subtypes=[subtype])
                self.assertEqual(_all_cards_grant_count(card), 1)

    def test_regular_card_uses_requested_count(self):
        card = _Card(CardType.POKEMON.value, subtypes=["Basic"])
        self.assertEqual(_all_cards_grant_count(card, regular_count=7), 7)


if __name__ == "__main__":
    unittest.main()
