from spirit.game.scripts.cards.SWSH3.Decidueye_13 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=35,
    rarity=Rarities.RarePromo,
    guid='3ac69dd3-7bc6-5fb2-b6a5-ef8185d66679',
    set_code='Promo_SWSH',
    key='Promo_SWSH',
    regulation_mark='D',
)

card.extra_attributes['200790'] = {'type': 'string', 'value': 'SWSH035'}
