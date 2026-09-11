from spirit.game.scripts.cards.XY1.VenusaurEX_1 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=123,
    rarity=Rarities.RarePromo,
    guid='ddc407c6-833b-501a-b441-384fd3302fb3',
    set_code='Promo_XY',
    key='Promo_XY',
    regulation_mark=None,
)
