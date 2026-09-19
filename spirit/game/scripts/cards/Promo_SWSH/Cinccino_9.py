from spirit.game.scripts.cards.SWSH1.Cinccino_147 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=9,
    rarity=Rarities.RarePromo,
    guid='253d9fd4-e492-53a8-aae9-458feef81620',
    set_code='Promo_SWSH',
    key='Promo_SWSH',
    regulation_mark='D',
)

card.extra_attributes['200790'] = {'type': 'string', 'value': 'SWSH009'}
