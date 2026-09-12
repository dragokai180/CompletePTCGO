"""Use the current errata for this HGSS printing."""
from spirit.game.scripts.cards.SWSH1.RareCandy_180 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities

card = reprint(
    base_card,
    collector_number=82,
    rarity=Rarities.Uncommon,
    guid='55ed0c69-c2c5-5b24-9e65-d71f15f22c14',
    set_code='HGSS2',
    key='HGSS2',
    regulation_mark=None,
)
