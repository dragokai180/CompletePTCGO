from spirit.game.scripts.cards.SWSH45.Morpeko_35 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=31,
    rarity=Rarities.RarePromo,
    guid='4a8c2672-d924-5eb6-a504-eef6498d3990',
    set_code='Promo_SWSH',
    key='Promo_SWSH',
    regulation_mark='D',
)

card.extra_attributes['200790'] = {'type': 'string', 'value': 'SWSH031'}
