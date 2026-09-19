from spirit.game.scripts.cards.SWSH7.NoivernV_117 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=148,
    rarity=Rarities.RarePromo,
    guid='6a62a753-eeaa-57c1-9884-4afbacdcc0bb',
    set_code='Promo_SWSH',
    key='Promo_SWSH',
    regulation_mark='E',
)

card.extra_attributes['200790'] = {'type': 'string', 'value': 'SWSH148'}
