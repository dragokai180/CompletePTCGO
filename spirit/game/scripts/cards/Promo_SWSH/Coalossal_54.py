from spirit.game.scripts.cards.SWSH2.Coalossal_107 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=54,
    rarity=Rarities.RarePromo,
    guid='3f014d42-0dc8-5e2c-b57b-52de23a4c9f1',
    set_code='Promo_SWSH',
    key='Promo_SWSH',
    regulation_mark='D',
)

card.extra_attributes['200790'] = {'type': 'string', 'value': 'SWSH054'}
