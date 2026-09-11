import unittest

from spirit.game.data_utils import def_for
from spirit.game.format_manager import FormatManager
from spirit.game.scripts.cards import loader as card_loader


STANDARD_GUID = "6402e830-7fed-4cd1-b172-2a320047c2bb"


class StandardFormatRotationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        card_loader.load_all()
        cls.manager = FormatManager()

    @staticmethod
    def card(set_code, display_name):
        return next(
            card for card in card_loader.cards
            if card.key == set_code
            and def_for(card.guid).display_name == display_name
        )

    def test_current_regulation_pokemon_is_legal(self):
        card = self.card("SV05", "Iron Leaves ex")
        self.assertTrue(self.manager.is_card_eventually_legal(STANDARD_GUID, card))

    def test_rotated_pokemon_does_not_inherit_name_reprint_legality(self):
        card = self.card("SVP", "Squawkabilly ex")
        self.assertFalse(self.manager.is_card_eventually_legal(STANDARD_GUID, card))

    def test_old_trainer_print_is_legal_when_current_reprint_exists(self):
        card = self.card("BW5", "Ultra Ball")
        self.assertTrue(self.manager.is_card_eventually_legal(STANDARD_GUID, card))

    def test_old_supporter_without_current_reprint_is_rotated(self):
        card = self.card("BW1", "Professor Juniper")
        self.assertFalse(self.manager.is_card_eventually_legal(STANDARD_GUID, card))


if __name__ == "__main__":
    unittest.main()
