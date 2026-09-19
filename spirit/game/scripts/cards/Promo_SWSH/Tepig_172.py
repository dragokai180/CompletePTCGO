from spirit.game.scripts.cards.SWSH5.Tepig_23 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=172,
    rarity=Rarities.RarePromo,
    guid='e80cfb3c-58cd-5bd8-83bc-d721200fb0c6',
    set_code='Promo_SWSH',
    key='Promo_SWSH',
    regulation_mark='E',
)

card.extra_attributes['200790'] = {'type': 'string', 'value': 'SWSH172'}
