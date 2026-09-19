from spirit.game.scripts.cards.SWSH1.Marnie_169 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=121,
    rarity=Rarities.RarePromo,
    guid='21c0a0ba-2692-5481-aa38-dd183cb57456',
    set_code='Promo_SWSH',
    key='Promo_SWSH',
    regulation_mark='D',
)

card.extra_attributes['200790'] = {'type': 'string', 'value': 'SWSH121'}
