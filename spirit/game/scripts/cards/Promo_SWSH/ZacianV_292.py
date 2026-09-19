from spirit.game.scripts.cards.SWSH1.ZacianV_138 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=292,
    rarity=Rarities.RarePromo,
    guid='d142d1c7-79c5-51bb-b6c0-b8a09227da74',
    set_code='Promo_SWSH',
    key='Promo_SWSH',
    regulation_mark='D',
)

card.extra_attributes['200790'] = {'type': 'string', 'value': 'SWSH292'}
