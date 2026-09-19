from spirit.game.scripts.cards.SWSH1.ZacianV_138 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=18,
    rarity=Rarities.RarePromo,
    guid='addbedfd-c378-59bc-acda-49b0093a27ab',
    set_code='Promo_SWSH',
    key='Promo_SWSH',
    regulation_mark='D',
)

card.extra_attributes['200790'] = {'type': 'string', 'value': 'SWSH018'}
