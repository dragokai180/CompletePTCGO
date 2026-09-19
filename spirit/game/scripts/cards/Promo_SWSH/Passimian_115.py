from spirit.game.scripts.cards.SWSH6.Passimian_88 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=115,
    rarity=Rarities.RarePromo,
    guid='f5a550e6-daf1-571c-b7cf-28bdc7b0af4f',
    set_code='Promo_SWSH',
    key='Promo_SWSH',
    regulation_mark='E',
)

card.extra_attributes['200790'] = {'type': 'string', 'value': 'SWSH115'}
