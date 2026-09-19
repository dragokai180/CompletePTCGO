from spirit.game.scripts.cards.SWSH4.AlakazamV_172 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=83,
    rarity=Rarities.RarePromo,
    guid='9ee504f7-8299-5149-9659-897a669ce696',
    set_code='Promo_SWSH',
    key='Promo_SWSH',
    regulation_mark='D',
)

card.extra_attributes['200790'] = {'type': 'string', 'value': 'SWSH083'}
