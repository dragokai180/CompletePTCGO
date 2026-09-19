from spirit.game.scripts.cards.SWSH9.ArceusVSTAR_123 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=307,
    rarity=Rarities.RarePromo,
    guid='3c585ac4-a499-5e03-96f5-d4c002f219e5',
    set_code='Promo_SWSH',
    key='Promo_SWSH',
    regulation_mark='F',
)

card.extra_attributes['200790'] = {'type': 'string', 'value': 'SWSH307'}
