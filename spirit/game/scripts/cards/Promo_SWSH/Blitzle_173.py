from spirit.game.scripts.cards.SWSH6.Blitzle_50 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=173,
    rarity=Rarities.RarePromo,
    guid='771fcf7f-5a29-5f2c-81b0-d806c5778704',
    set_code='Promo_SWSH',
    key='Promo_SWSH',
    regulation_mark='E',
)

card.extra_attributes['200790'] = {'type': 'string', 'value': 'SWSH173'}
