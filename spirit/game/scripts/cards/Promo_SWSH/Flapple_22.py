from spirit.game.scripts.cards.SWSH2.Flapple_22 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=22,
    rarity=Rarities.RarePromo,
    guid='a8db1d24-1995-5177-aa89-dcc5a2c0fc35',
    set_code='Promo_SWSH',
    key='Promo_SWSH',
    regulation_mark='D',
)

card.extra_attributes['200790'] = {'type': 'string', 'value': 'SWSH022'}
