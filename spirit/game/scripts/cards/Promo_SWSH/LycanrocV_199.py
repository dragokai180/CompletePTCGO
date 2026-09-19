from spirit.game.scripts.cards.SWSH7.LycanrocV_91 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=199,
    rarity=Rarities.RarePromo,
    guid='bae5a75c-f4f6-5b9a-b12b-bf1f82ba1961',
    set_code='Promo_SWSH',
    key='Promo_SWSH',
    regulation_mark='E',
)

card.extra_attributes['200790'] = {'type': 'string', 'value': 'SWSH199'}
