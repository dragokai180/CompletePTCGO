from spirit.game.scripts.cards.SWSH9.LumineonV_40 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=250,
    rarity=Rarities.RarePromo,
    guid='dc27a1aa-003e-5106-9311-80e5224185c3',
    set_code='Promo_SWSH',
    key='Promo_SWSH',
    regulation_mark='F',
)

card.extra_attributes['200790'] = {'type': 'string', 'value': 'SWSH250'}
