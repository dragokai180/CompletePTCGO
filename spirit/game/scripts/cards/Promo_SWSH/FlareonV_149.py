from spirit.game.scripts.cards.SWSH7.FlareonV_169 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=149,
    rarity=Rarities.RarePromo,
    guid='2b58b9c6-3694-5a52-8a67-b7345b538693',
    set_code='Promo_SWSH',
    key='Promo_SWSH',
    regulation_mark='E',
)

card.extra_attributes['200790'] = {'type': 'string', 'value': 'SWSH149'}
