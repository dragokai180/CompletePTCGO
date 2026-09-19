from spirit.game.scripts.cards.CZ.GlaceonV_38 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=196,
    rarity=Rarities.RarePromo,
    guid='80282c8e-cdd5-5164-bf15-b4e0c5a96c9f',
    set_code='Promo_SWSH',
    key='Promo_SWSH',
    regulation_mark='F',
)

card.extra_attributes['200790'] = {'type': 'string', 'value': 'SWSH196'}
