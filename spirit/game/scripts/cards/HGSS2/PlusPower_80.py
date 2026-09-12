"""Use the current errata for this HGSS printing."""
from spirit.game.scripts.cards.BW1.PlusPower_96 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities

card = reprint(
    base_card,
    collector_number=80,
    rarity=Rarities.Uncommon,
    guid='d52715cc-ac2c-5677-be96-4193b0a7721a',
    set_code='HGSS2',
    key='HGSS2',
    regulation_mark=None,
)
