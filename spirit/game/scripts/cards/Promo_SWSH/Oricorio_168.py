from spirit.game.scripts.cards.SWSH8.Oricorio_42 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=168,
    rarity=Rarities.RarePromo,
    guid='ef4b3395-b7b8-51d0-b857-31b98be6ffc4',
    set_code='Promo_SWSH',
    key='Promo_SWSH',
    regulation_mark='E',
)

card.extra_attributes['200790'] = {'type': 'string', 'value': 'SWSH168'}
