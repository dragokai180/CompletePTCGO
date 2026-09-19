from spirit.game.scripts.cards.SWSH2.RillaboomV_17 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=14,
    rarity=Rarities.RarePromo,
    guid='c407bb4a-bff6-551f-9e28-454f11705e72',
    set_code='Promo_SWSH',
    key='Promo_SWSH',
    regulation_mark='D',
)

card.extra_attributes['200790'] = {'type': 'string', 'value': 'SWSH014'}
