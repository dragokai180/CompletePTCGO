from spirit.game.scripts.cards.PGO.AlolanExeggutorV_5 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=225,
    rarity=Rarities.RarePromo,
    guid='ab562d07-a911-52f2-82fa-44389198627c',
    set_code='Promo_SWSH',
    key='Promo_SWSH',
    regulation_mark='F',
)

card.extra_attributes['200790'] = {'type': 'string', 'value': 'SWSH225'}
