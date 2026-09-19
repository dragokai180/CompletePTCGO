from spirit.game.scripts.cards.SWSH7.VaporeonV_172 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=181,
    rarity=Rarities.RarePromo,
    guid='cc1190f0-f350-56ef-b0bd-581c516eae09',
    set_code='Promo_SWSH',
    key='Promo_SWSH',
    regulation_mark='E',
)

card.extra_attributes['200790'] = {'type': 'string', 'value': 'SWSH181'}
