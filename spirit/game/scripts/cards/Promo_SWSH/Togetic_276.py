from spirit.game.scripts.cards.SWSH10.Togetic_56 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=276,
    rarity=Rarities.RarePromo,
    guid='65afa2a3-444b-5a4e-bc68-fcbaad09cc0b',
    set_code='Promo_SWSH',
    key='Promo_SWSH',
    regulation_mark='F',
)

card.extra_attributes['200790'] = {'type': 'string', 'value': 'SWSH276'}
