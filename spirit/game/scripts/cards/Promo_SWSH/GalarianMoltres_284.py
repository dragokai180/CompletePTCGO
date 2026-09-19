from spirit.game.scripts.cards.SWSH7.GalarianMoltres_93 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=284,
    rarity=Rarities.RarePromo,
    guid='16487241-691b-57d0-928d-646bfc52fc56',
    set_code='Promo_SWSH',
    key='Promo_SWSH',
    regulation_mark='E',
)

card.extra_attributes['200790'] = {'type': 'string', 'value': 'SWSH284'}
