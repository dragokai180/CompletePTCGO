from spirit.game.scripts.cards.SWSH3.Kangaskhan_133 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=38,
    rarity=Rarities.RarePromo,
    guid='4df3a30f-1cea-5da2-b6e1-c09ad96648bf',
    set_code='Promo_SWSH',
    key='Promo_SWSH',
    regulation_mark='D',
)

card.extra_attributes['200790'] = {'type': 'string', 'value': 'SWSH038'}
