from spirit.game.scripts.cards.SWSH2.Luxray_62 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=23,
    rarity=Rarities.RarePromo,
    guid='6c0e5f7f-659d-57c0-883a-e52519d40f52',
    set_code='Promo_SWSH',
    key='Promo_SWSH',
    regulation_mark='D',
)

card.extra_attributes['200790'] = {'type': 'string', 'value': 'SWSH023'}
