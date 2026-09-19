from spirit.game.scripts.cards.SWSH7.JolteonV_177 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=183,
    rarity=Rarities.RarePromo,
    guid='3739b944-b4d3-5a80-8089-817ba897be13',
    set_code='Promo_SWSH',
    key='Promo_SWSH',
    regulation_mark='E',
)

card.extra_attributes['200790'] = {'type': 'string', 'value': 'SWSH183'}
