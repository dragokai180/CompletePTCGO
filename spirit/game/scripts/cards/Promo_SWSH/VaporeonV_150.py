from spirit.game.scripts.cards.SWSH7.VaporeonV_172 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=150,
    rarity=Rarities.RarePromo,
    guid='ef881381-a1d2-5b27-aafc-7dd4c4b92fc9',
    set_code='Promo_SWSH',
    key='Promo_SWSH',
    regulation_mark='E',
)

card.extra_attributes['200790'] = {'type': 'string', 'value': 'SWSH150'}
