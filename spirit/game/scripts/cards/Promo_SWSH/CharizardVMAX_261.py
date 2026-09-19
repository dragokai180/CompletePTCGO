from spirit.game.scripts.cards.SWSH3.CharizardVMAX_20 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=261,
    rarity=Rarities.RarePromo,
    guid='2d24166d-98c7-5cdf-8159-f57d18007ea3',
    set_code='Promo_SWSH',
    key='Promo_SWSH',
    regulation_mark='D',
)

card.extra_attributes['200790'] = {'type': 'string', 'value': 'SWSH261'}
