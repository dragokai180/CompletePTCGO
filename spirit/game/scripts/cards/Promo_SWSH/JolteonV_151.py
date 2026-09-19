from spirit.game.scripts.cards.SWSH7.JolteonV_177 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=151,
    rarity=Rarities.RarePromo,
    guid='192a737b-8b63-5451-bc13-1fa5aa6f81d0',
    set_code='Promo_SWSH',
    key='Promo_SWSH',
    regulation_mark='E',
)

card.extra_attributes['200790'] = {'type': 'string', 'value': 'SWSH151'}
