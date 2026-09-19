from spirit.game.scripts.cards.SWSH11.Machamp_88 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=243,
    rarity=Rarities.RarePromo,
    guid='2147ce47-eae9-5f05-839a-67352d3d4468',
    set_code='Promo_SWSH',
    key='Promo_SWSH',
    regulation_mark='F',
)

card.extra_attributes['200790'] = {'type': 'string', 'value': 'SWSH243'}
