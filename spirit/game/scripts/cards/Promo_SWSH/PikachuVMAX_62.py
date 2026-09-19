from spirit.game.scripts.cards.SWSH4.PikachuVMAX_44 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=62,
    rarity=Rarities.RarePromo,
    guid='ea1fac0a-1a3d-5926-be55-f6a50bc4a400',
    set_code='Promo_SWSH',
    key='Promo_SWSH',
    regulation_mark='D',
)

card.extra_attributes['200790'] = {'type': 'string', 'value': 'SWSH062'}
