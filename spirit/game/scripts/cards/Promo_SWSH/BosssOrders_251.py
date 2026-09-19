from spirit.game.scripts.cards.SWSH2.BosssOrders_154 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=251,
    rarity=Rarities.RarePromo,
    guid='1e8c0f04-d1f2-5579-90ef-1549a64bf163',
    set_code='Promo_SWSH',
    key='Promo_SWSH',
    regulation_mark='F',
)

card.extra_attributes['200790'] = {'type': 'string', 'value': 'SWSH251'}
