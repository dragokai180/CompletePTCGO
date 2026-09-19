from spirit.game.scripts.cards.SWSH35.Machamp_26 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=53,
    rarity=Rarities.RarePromo,
    guid='7bdf7423-4518-53f3-a937-e1b6c2dfc3de',
    set_code='Promo_SWSH',
    key='Promo_SWSH',
    regulation_mark='D',
)

card.extra_attributes['200790'] = {'type': 'string', 'value': 'SWSH053'}
