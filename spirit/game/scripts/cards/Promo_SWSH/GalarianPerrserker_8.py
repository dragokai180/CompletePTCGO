from spirit.game.scripts.cards.SWSH1.GalarianPerrserker_128 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=8,
    rarity=Rarities.RarePromo,
    guid='e3402656-e9a8-5f5f-aa4a-6091c754356e',
    set_code='Promo_SWSH',
    key='Promo_SWSH',
    regulation_mark='D',
)

card.extra_attributes['200790'] = {'type': 'string', 'value': 'SWSH008'}
