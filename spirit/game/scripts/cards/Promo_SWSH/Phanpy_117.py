from spirit.game.scripts.cards.SWSH4.Phanpy_86 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=117,
    rarity=Rarities.RarePromo,
    guid='479daa3e-1639-5d57-ae7b-9d3265cb8439',
    set_code='Promo_SWSH',
    key='Promo_SWSH',
    regulation_mark='D',
)

card.extra_attributes['200790'] = {'type': 'string', 'value': 'SWSH117'}
