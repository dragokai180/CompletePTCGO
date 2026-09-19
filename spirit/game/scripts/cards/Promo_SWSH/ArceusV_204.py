from spirit.game.scripts.cards.SWSH9.ArceusV_122 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=204,
    rarity=Rarities.RarePromo,
    guid='e06ae162-0998-5afb-bd5f-f95018e13bd4',
    set_code='Promo_SWSH',
    key='Promo_SWSH',
    regulation_mark='F',
)

card.extra_attributes['200790'] = {'type': 'string', 'value': 'SWSH204'}
