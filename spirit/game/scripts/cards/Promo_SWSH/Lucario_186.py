from spirit.game.scripts.cards.SWSH9.Lucario_79 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=186,
    rarity=Rarities.RarePromo,
    guid='f1c92950-24e0-5346-9906-df7da2573b40',
    set_code='Promo_SWSH',
    key='Promo_SWSH',
    regulation_mark='F',
)

card.extra_attributes['200790'] = {'type': 'string', 'value': 'SWSH186'}
