from spirit.game.scripts.cards.SWSH7.EspeonV_64 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=201,
    rarity=Rarities.RarePromo,
    guid='c45a61e7-0485-5e29-8616-2ae766c73d52',
    set_code='Promo_SWSH',
    key='Promo_SWSH',
    regulation_mark='E',
)

card.extra_attributes['200790'] = {'type': 'string', 'value': 'SWSH201'}
