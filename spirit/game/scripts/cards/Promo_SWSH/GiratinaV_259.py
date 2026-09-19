from spirit.game.scripts.cards.SWSH11.GiratinaV_130 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=259,
    rarity=Rarities.RarePromo,
    guid='28677dc8-3f4e-555b-943e-6f47d31b8288',
    set_code='Promo_SWSH',
    key='Promo_SWSH',
    regulation_mark='F',
)

card.extra_attributes['200790'] = {'type': 'string', 'value': 'SWSH259'}
