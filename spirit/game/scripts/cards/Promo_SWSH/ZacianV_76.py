from spirit.game.scripts.cards.SWSH1.ZacianV_138 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=76,
    rarity=Rarities.RarePromo,
    guid='bff31b22-f097-5a73-b2c2-3a775900279a',
    set_code='Promo_SWSH',
    key='Promo_SWSH',
    regulation_mark='D',
)

card.extra_attributes['200790'] = {'type': 'string', 'value': 'SWSH076'}
