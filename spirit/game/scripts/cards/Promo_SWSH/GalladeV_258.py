from spirit.game.scripts.cards.SWSH11.GalladeV_181 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=258,
    rarity=Rarities.RarePromo,
    guid='9a9dde2c-417b-5c3e-a2a1-5894f18be66b',
    set_code='Promo_SWSH',
    key='Promo_SWSH',
    regulation_mark='F',
)

card.extra_attributes['200790'] = {'type': 'string', 'value': 'SWSH258'}
