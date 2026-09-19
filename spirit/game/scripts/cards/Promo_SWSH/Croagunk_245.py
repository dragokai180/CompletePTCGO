from spirit.game.scripts.cards.SWSH8.Croagunk_165 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=245,
    rarity=Rarities.RarePromo,
    guid='30b5bbb5-7e19-5b81-859e-35298907d95a',
    set_code='Promo_SWSH',
    key='Promo_SWSH',
    regulation_mark='E',
)

card.extra_attributes['200790'] = {'type': 'string', 'value': 'SWSH245'}
