from spirit.game.scripts.cards.SWSH1.Drednaw_61 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=47,
    rarity=Rarities.RarePromo,
    guid='6303d7c9-b778-5e3e-a36b-f2d87b961563',
    set_code='Promo_SWSH',
    key='Promo_SWSH',
    regulation_mark='D',
)

card.extra_attributes['200790'] = {'type': 'string', 'value': 'SWSH047'}
