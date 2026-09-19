from spirit.game.scripts.cards.SWSH10.OriginFormePalkiaV_39 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=253,
    rarity=Rarities.RarePromo,
    guid='b1c6d4e3-5953-542c-ae81-9f99612248d8',
    set_code='Promo_SWSH',
    key='Promo_SWSH',
    regulation_mark='F',
)

card.extra_attributes['200790'] = {'type': 'string', 'value': 'SWSH253'}
