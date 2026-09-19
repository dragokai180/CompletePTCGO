from spirit.game.scripts.cards.SWSH2.Garbodor_118 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=25,
    rarity=Rarities.RarePromo,
    guid='08fc216a-dee8-589b-95e7-b5d4342cf860',
    set_code='Promo_SWSH',
    key='Promo_SWSH',
    regulation_mark='D',
)

card.extra_attributes['200790'] = {'type': 'string', 'value': 'SWSH025'}
