from spirit.game.scripts.cards.SWSH7.GalarianArticuno_63 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=282,
    rarity=Rarities.RarePromo,
    guid='dcb4387c-5b11-55e5-b1e4-5cc30c6ef210',
    set_code='Promo_SWSH',
    key='Promo_SWSH',
    regulation_mark='E',
)

card.extra_attributes['200790'] = {'type': 'string', 'value': 'SWSH282'}
