from spirit.game.scripts.cards.SWSH3.Arctozolt_66 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=36,
    rarity=Rarities.RarePromo,
    guid='2e82bced-0107-5c5b-8380-96ebbab0bb86',
    set_code='Promo_SWSH',
    key='Promo_SWSH',
    regulation_mark='D',
)

card.extra_attributes['200790'] = {'type': 'string', 'value': 'SWSH036'}
