from spirit.game.scripts.cards.SWSH12.RegidragoV_135 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=281,
    rarity=Rarities.RarePromo,
    guid='7fd3a126-682e-54c8-b2c5-38e0fcdd41c3',
    set_code='Promo_SWSH',
    key='Promo_SWSH',
    regulation_mark='F',
)

card.extra_attributes['200790'] = {'type': 'string', 'value': 'SWSH281'}
