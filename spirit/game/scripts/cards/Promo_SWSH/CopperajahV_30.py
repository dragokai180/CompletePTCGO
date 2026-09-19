from spirit.game.scripts.cards.SWSH2.CopperajahV_136 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=30,
    rarity=Rarities.RarePromo,
    guid='ee00519f-cdf7-5eec-a00e-66cfc822a92a',
    set_code='Promo_SWSH',
    key='Promo_SWSH',
    regulation_mark='D',
)

card.extra_attributes['200790'] = {'type': 'string', 'value': 'SWSH030'}
