from spirit.game.scripts.cards.SWSH45.Morpeko_35 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=116,
    rarity=Rarities.RarePromo,
    guid='7b5c8cbc-84f7-539b-811f-38d9f8e1705f',
    set_code='Promo_SWSH',
    key='Promo_SWSH',
    regulation_mark='D',
)

card.extra_attributes['200790'] = {'type': 'string', 'value': 'SWSH116'}
