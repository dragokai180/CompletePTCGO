from spirit.game.scripts.cards.CZ.ZeraoraV_53 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=263,
    rarity=Rarities.RarePromo,
    guid='37f4a6c0-7a05-5eac-99ee-21b9b858b686',
    set_code='Promo_SWSH',
    key='Promo_SWSH',
    regulation_mark='F',
)

card.extra_attributes['200790'] = {'type': 'string', 'value': 'SWSH263'}
