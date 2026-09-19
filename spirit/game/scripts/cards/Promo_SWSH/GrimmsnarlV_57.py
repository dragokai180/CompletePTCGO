from spirit.game.scripts.cards.SWSH3.GrimmsnarlV_114 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=57,
    rarity=Rarities.RarePromo,
    guid='510d1295-c7c8-53f4-a24a-84203ac228b1',
    set_code='Promo_SWSH',
    key='Promo_SWSH',
    regulation_mark='D',
)

card.extra_attributes['200790'] = {'type': 'string', 'value': 'SWSH057'}
