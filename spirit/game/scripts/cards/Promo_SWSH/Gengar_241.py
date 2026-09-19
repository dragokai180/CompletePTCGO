from spirit.game.scripts.cards.SWSH11.Gengar_66 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=241,
    rarity=Rarities.RarePromo,
    guid='74a01dca-5ce3-5022-90d6-79ae84c3db6d',
    set_code='Promo_SWSH',
    key='Promo_SWSH',
    regulation_mark='F',
)

card.extra_attributes['200790'] = {'type': 'string', 'value': 'SWSH241'}
