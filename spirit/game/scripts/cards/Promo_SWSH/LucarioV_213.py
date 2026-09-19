from spirit.game.scripts.cards.SWSH10.LucarioV_78 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=213,
    rarity=Rarities.RarePromo,
    guid='73277516-64a8-5981-b475-9ef7c6c38844',
    set_code='Promo_SWSH',
    key='Promo_SWSH',
    regulation_mark='F',
)

card.extra_attributes['200790'] = {'type': 'string', 'value': 'SWSH213'}
