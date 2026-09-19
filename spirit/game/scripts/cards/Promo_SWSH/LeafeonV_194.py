from spirit.game.scripts.cards.CZ.LeafeonV_13 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=194,
    rarity=Rarities.RarePromo,
    guid='bbd27a99-b6c3-5a26-940e-ce370c3747a7',
    set_code='Promo_SWSH',
    key='Promo_SWSH',
    regulation_mark='F',
)

card.extra_attributes['200790'] = {'type': 'string', 'value': 'SWSH194'}
