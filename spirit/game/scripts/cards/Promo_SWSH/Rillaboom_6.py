from spirit.game.scripts.cards.SWSH1.Rillaboom_14 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=6,
    rarity=Rarities.RarePromo,
    guid='bd45cde5-216c-5550-9134-c3a275f3a08c',
    set_code='Promo_SWSH',
    key='Promo_SWSH',
    regulation_mark='D',
)

card.extra_attributes['200790'] = {'type': 'string', 'value': 'SWSH006'}
