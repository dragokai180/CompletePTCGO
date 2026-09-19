from spirit.game.scripts.cards.SWSH9.ArceusV_122 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=306,
    rarity=Rarities.RarePromo,
    guid='ccefc05f-01ae-59d6-ac33-b4a2069419d8',
    set_code='Promo_SWSH',
    key='Promo_SWSH',
    regulation_mark='F',
)

card.extra_attributes['200790'] = {'type': 'string', 'value': 'SWSH306'}
