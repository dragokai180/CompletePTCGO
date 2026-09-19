from spirit.game.scripts.cards.SWSH6.GalarianRapidashV_167 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=111,
    rarity=Rarities.RarePromo,
    guid='e57e0934-24c2-578e-90e7-95e0a021dc60',
    set_code='Promo_SWSH',
    key='Promo_SWSH',
    regulation_mark='E',
)

card.extra_attributes['200790'] = {'type': 'string', 'value': 'SWSH111'}
