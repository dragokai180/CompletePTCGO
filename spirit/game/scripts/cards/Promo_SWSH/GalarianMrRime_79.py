from spirit.game.scripts.cards.SWSH3.GalarianMrRime_36 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=79,
    rarity=Rarities.RarePromo,
    guid='f70ad4d2-1337-5edc-be93-fc617c30c2c6',
    set_code='Promo_SWSH',
    key='Promo_SWSH',
    regulation_mark='D',
)

card.extra_attributes['200790'] = {'type': 'string', 'value': 'SWSH079'}
