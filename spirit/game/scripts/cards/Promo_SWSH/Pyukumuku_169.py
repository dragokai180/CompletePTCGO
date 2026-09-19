from spirit.game.scripts.cards.SWSH8.Pyukumuku_77 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=169,
    rarity=Rarities.RarePromo,
    guid='ca8290c0-fe43-5879-82d6-17c9070d3d4f',
    set_code='Promo_SWSH',
    key='Promo_SWSH',
    regulation_mark='E',
)

card.extra_attributes['200790'] = {'type': 'string', 'value': 'SWSH169'}
