from spirit.game.scripts.cards.SWSH2.InteleonV_49 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=16,
    rarity=Rarities.RarePromo,
    guid='c26e8ec6-de6a-5483-92a2-45731ba7640b',
    set_code='Promo_SWSH',
    key='Promo_SWSH',
    regulation_mark='D',
)

card.extra_attributes['200790'] = {'type': 'string', 'value': 'SWSH016'}
