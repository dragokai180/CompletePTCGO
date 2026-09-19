from spirit.game.scripts.cards.SWSH2.Duraludon_138 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=60,
    rarity=Rarities.RarePromo,
    guid='82e2d3b3-e782-5ff3-b8dd-277cd6738845',
    set_code='Promo_SWSH',
    key='Promo_SWSH',
    regulation_mark='D',
)

card.extra_attributes['200790'] = {'type': 'string', 'value': 'SWSH060'}
