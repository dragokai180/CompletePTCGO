from spirit.game.scripts.cards.SWSH4.GalarianSirfetchdV_174 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=43,
    rarity=Rarities.RarePromo,
    guid='eaa8c3b7-ea1a-5e9e-9a6b-776c0411ca06',
    set_code='Promo_SWSH',
    key='Promo_SWSH',
    regulation_mark='D',
)

card.extra_attributes['200790'] = {'type': 'string', 'value': 'SWSH043'}
