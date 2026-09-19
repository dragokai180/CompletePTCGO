from spirit.game.scripts.cards.SWSH9.Bibarel_121 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=188,
    rarity=Rarities.RarePromo,
    guid='2788a73d-95b8-578c-b5b3-72729e18d158',
    set_code='Promo_SWSH',
    key='Promo_SWSH',
    regulation_mark='F',
)

card.extra_attributes['200790'] = {'type': 'string', 'value': 'SWSH188'}
