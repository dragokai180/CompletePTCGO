"""Additional Scarlet & Violet Energy printing."""
from spirit.game.data_utils import reprint
from spirit.game.scripts.cards.SVE.BasicFightingEnergy_6 import card as base_card

card = reprint(
    base_card,
    set_code="SVE",
    key="SVE",
    collector_number=22,
    regulation_mark=None,
)
