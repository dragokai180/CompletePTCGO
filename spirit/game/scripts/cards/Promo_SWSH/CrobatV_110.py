from spirit.game.scripts.cards.SWSH3.CrobatV_104 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=110,
    rarity=Rarities.RarePromo,
    guid='8d78a637-6f5a-5fc9-b18f-6d992eb0a135',
    set_code='Promo_SWSH',
    key='Promo_SWSH',
    regulation_mark='D',
)

card.extra_attributes['200790'] = {'type': 'string', 'value': 'SWSH110'}
