from spirit.game.scripts.cards.SWSH8.Latias_193 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=171,
    rarity=Rarities.RarePromo,
    guid='634ee80f-da30-53ee-aa52-e0ad3de8c0f5',
    set_code='Promo_SWSH',
    key='Promo_SWSH',
    regulation_mark='E',
)

card.extra_attributes['200790'] = {'type': 'string', 'value': 'SWSH171'}
