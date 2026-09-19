from spirit.game.scripts.cards.SWSH2.EldegossV_19 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=84,
    rarity=Rarities.RarePromo,
    guid='912500c3-21b2-552a-98b8-46fdb17b26aa',
    set_code='Promo_SWSH',
    key='Promo_SWSH',
    regulation_mark='D',
)

card.extra_attributes['200790'] = {'type': 'string', 'value': 'SWSH084'}
