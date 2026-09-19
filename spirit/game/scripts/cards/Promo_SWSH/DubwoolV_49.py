from spirit.game.scripts.cards.SWSH2.DubwoolV_153 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=49,
    rarity=Rarities.RarePromo,
    guid='1f79b049-33b0-58ea-a6c1-110fb681d843',
    set_code='Promo_SWSH',
    key='Promo_SWSH',
    regulation_mark='D',
)

card.extra_attributes['200790'] = {'type': 'string', 'value': 'SWSH049'}
