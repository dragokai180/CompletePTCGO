from spirit.game.scripts.cards.SWSH10.Cranidos_76 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=274,
    rarity=Rarities.RarePromo,
    guid='2af87b57-917c-5098-b712-d4ea5bf34583',
    set_code='Promo_SWSH',
    key='Promo_SWSH',
    regulation_mark='F',
)

card.extra_attributes['200790'] = {'type': 'string', 'value': 'SWSH274'}
