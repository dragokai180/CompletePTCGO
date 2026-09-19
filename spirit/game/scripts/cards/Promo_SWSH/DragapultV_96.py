from spirit.game.scripts.cards.SWSH2.DragapultV_92 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=96,
    rarity=Rarities.RarePromo,
    guid='e2a00640-c782-526a-ac6b-9e667256e6fe',
    set_code='Promo_SWSH',
    key='Promo_SWSH',
    regulation_mark='D',
)

card.extra_attributes['200790'] = {'type': 'string', 'value': 'SWSH096'}
