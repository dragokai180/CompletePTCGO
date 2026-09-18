"""Additional Scarlet & Violet Energy printing."""
from spirit.game.data_utils import reprint
from spirit.game.scripts.cards.SVE.BasicFireEnergy_2 import card as base_card

card = reprint(
    base_card,
    set_code="SVE",
    key="SVE",
    collector_number=18,
    regulation_mark=None,
)
