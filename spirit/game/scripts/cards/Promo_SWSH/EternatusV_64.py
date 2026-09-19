from spirit.game.scripts.cards.SWSH3.EternatusV_116 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=64,
    rarity=Rarities.RarePromo,
    guid='7e35f0c3-78d7-57fb-a495-43e8ba8ce03e',
    set_code='Promo_SWSH',
    key='Promo_SWSH',
    regulation_mark='D',
)

card.extra_attributes['200790'] = {'type': 'string', 'value': 'SWSH064'}
