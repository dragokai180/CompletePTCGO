from spirit.game.scripts.cards.XY1.VenusaurEX_1 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=28,
    rarity=Rarities.RarePromo,
    guid='cf0a3b1b-3103-5282-8294-127bf1110387',
    set_code='Promo_XY',
    key='Promo_XY',
    regulation_mark=None,
)
