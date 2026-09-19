from spirit.game.scripts.cards.CZ.ZeraoraVMAX_54 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=264,
    rarity=Rarities.RarePromo,
    guid='fda25532-dfbc-56af-8fa0-55a5d7f1098b',
    set_code='Promo_SWSH',
    key='Promo_SWSH',
    regulation_mark='F',
)

card.extra_attributes['200790'] = {'type': 'string', 'value': 'SWSH264'}
