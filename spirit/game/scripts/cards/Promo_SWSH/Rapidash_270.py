from spirit.game.scripts.cards.SWSH12.Rapidash_22 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=270,
    rarity=Rarities.RarePromo,
    guid='1dbde1c3-1b7a-57cc-8469-56747db60d78',
    set_code='Promo_SWSH',
    key='Promo_SWSH',
    regulation_mark='F',
)

card.extra_attributes['200790'] = {'type': 'string', 'value': 'SWSH270'}
