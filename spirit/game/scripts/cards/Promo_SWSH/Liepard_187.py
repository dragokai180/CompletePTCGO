from spirit.game.scripts.cards.SWSH9.Liepard_91 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=187,
    rarity=Rarities.RarePromo,
    guid='79dce55d-85c8-5743-b883-08a75d0319a9',
    set_code='Promo_SWSH',
    key='Promo_SWSH',
    regulation_mark='F',
)

card.extra_attributes['200790'] = {'type': 'string', 'value': 'SWSH187'}
