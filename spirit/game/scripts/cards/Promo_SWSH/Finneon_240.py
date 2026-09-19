from spirit.game.scripts.cards.SWSH11.Finneon_40 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=240,
    rarity=Rarities.RarePromo,
    guid='3c8974f1-cb03-5472-b9bc-5d76fc174767',
    set_code='Promo_SWSH',
    key='Promo_SWSH',
    regulation_mark='F',
)

card.extra_attributes['200790'] = {'type': 'string', 'value': 'SWSH240'}
