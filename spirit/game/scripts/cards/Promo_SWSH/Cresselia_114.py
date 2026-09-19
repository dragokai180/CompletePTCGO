from spirit.game.scripts.cards.SWSH6.Cresselia_64 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=114,
    rarity=Rarities.RarePromo,
    guid='3124d7c7-cce1-5c80-bdae-7b545657879d',
    set_code='Promo_SWSH',
    key='Promo_SWSH',
    regulation_mark='E',
)

card.extra_attributes['200790'] = {'type': 'string', 'value': 'SWSH114'}
