from spirit.game.scripts.cards.SWSH4.OrbeetleV_20 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=78,
    rarity=Rarities.RarePromo,
    guid='21263de3-a643-5a45-a960-8221ea1db03a',
    set_code='Promo_SWSH',
    key='Promo_SWSH',
    regulation_mark='D',
)

card.extra_attributes['200790'] = {'type': 'string', 'value': 'SWSH078'}
