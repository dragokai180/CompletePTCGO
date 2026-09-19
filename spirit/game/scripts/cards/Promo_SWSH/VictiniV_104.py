from spirit.game.scripts.cards.SWSH1.VictiniV_25 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=104,
    rarity=Rarities.RarePromo,
    guid='2a3fdad0-f0ba-532f-a561-9da9b437df94',
    set_code='Promo_SWSH',
    key='Promo_SWSH',
    regulation_mark='D',
)

card.extra_attributes['200790'] = {'type': 'string', 'value': 'SWSH104'}
