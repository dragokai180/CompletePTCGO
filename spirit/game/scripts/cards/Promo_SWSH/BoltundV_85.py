from spirit.game.scripts.cards.SWSH2.BoltundV_67 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=85,
    rarity=Rarities.RarePromo,
    guid='97dc8450-de33-5e43-bc86-68c03c142987',
    set_code='Promo_SWSH',
    key='Promo_SWSH',
    regulation_mark='D',
)

card.extra_attributes['200790'] = {'type': 'string', 'value': 'SWSH085'}
