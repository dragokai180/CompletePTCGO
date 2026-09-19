from spirit.game.scripts.cards.SWSH8.Deoxys_120 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=170,
    rarity=Rarities.RarePromo,
    guid='a1d01713-85d3-5a7b-ab83-3e9b86900065',
    set_code='Promo_SWSH',
    key='Promo_SWSH',
    regulation_mark='E',
)

card.extra_attributes['200790'] = {'type': 'string', 'value': 'SWSH170'}
