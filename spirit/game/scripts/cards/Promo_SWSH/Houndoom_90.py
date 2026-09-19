from spirit.game.scripts.cards.SWSH5.Houndoom_96 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=90,
    rarity=Rarities.RarePromo,
    guid='6c1c96f7-b4cd-5a72-a04c-6fe1711e6d55',
    set_code='Promo_SWSH',
    key='Promo_SWSH',
    regulation_mark='E',
)

card.extra_attributes['200790'] = {'type': 'string', 'value': 'SWSH090'}
