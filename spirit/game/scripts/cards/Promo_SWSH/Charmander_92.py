from spirit.game.scripts.cards.SWSH4.Charmander_23 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=92,
    rarity=Rarities.RarePromo,
    guid='813cd242-6a66-5cd5-af4f-8e03844b2534',
    set_code='Promo_SWSH',
    key='Promo_SWSH',
    regulation_mark='D',
)

card.extra_attributes['200790'] = {'type': 'string', 'value': 'SWSH092'}
