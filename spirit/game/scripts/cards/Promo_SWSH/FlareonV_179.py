from spirit.game.scripts.cards.SWSH7.FlareonV_169 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=179,
    rarity=Rarities.RarePromo,
    guid='06ca8e2a-0b5c-527a-84f1-7f7709eb3f4a',
    set_code='Promo_SWSH',
    key='Promo_SWSH',
    regulation_mark='E',
)

card.extra_attributes['200790'] = {'type': 'string', 'value': 'SWSH179'}
