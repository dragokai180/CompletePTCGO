from spirit.game.scripts.cards.SWSH3.Polteageist_83 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=81,
    rarity=Rarities.RarePromo,
    guid='3463d472-e43f-5cab-98e1-6ed02fdbb6d6',
    set_code='Promo_SWSH',
    key='Promo_SWSH',
    regulation_mark='D',
)

card.extra_attributes['200790'] = {'type': 'string', 'value': 'SWSH081'}
