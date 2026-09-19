from spirit.game.scripts.cards.SWSH3.Dedenne_78 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=80,
    rarity=Rarities.RarePromo,
    guid='c40b4a15-3a07-5b09-b339-ffa4951c5f15',
    set_code='Promo_SWSH',
    key='Promo_SWSH',
    regulation_mark='D',
)

card.extra_attributes['200790'] = {'type': 'string', 'value': 'SWSH080'}
