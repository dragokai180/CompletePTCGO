from spirit.game.scripts.cards.SWSH3.EternatusV_116 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=44,
    rarity=Rarities.RarePromo,
    guid='0bdd48a7-6b43-5d93-b1f3-6786dea37da2',
    set_code='Promo_SWSH',
    key='Promo_SWSH',
    regulation_mark='D',
)

card.extra_attributes['200790'] = {'type': 'string', 'value': 'SWSH044'}
