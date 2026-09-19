from spirit.game.scripts.cards.SWSH11.Comfey_79 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=242,
    rarity=Rarities.RarePromo,
    guid='5ee58cd9-3dc5-543e-ad80-4b62c52f3dc6',
    set_code='Promo_SWSH',
    key='Promo_SWSH',
    regulation_mark='F',
)

card.extra_attributes['200790'] = {'type': 'string', 'value': 'SWSH242'}
