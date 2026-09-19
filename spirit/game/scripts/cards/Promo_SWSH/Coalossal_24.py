from spirit.game.scripts.cards.SWSH2.Coalossal_107 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=24,
    rarity=Rarities.RarePromo,
    guid='997f9414-1c4f-5424-b1b0-b572b4bd7e7c',
    set_code='Promo_SWSH',
    key='Promo_SWSH',
    regulation_mark='D',
)

card.extra_attributes['200790'] = {'type': 'string', 'value': 'SWSH024'}
