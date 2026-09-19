from spirit.game.scripts.cards.PGO.Blanche_64 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=227,
    rarity=Rarities.RarePromo,
    guid='7486fd26-8dab-528d-ae56-d3c1023e2324',
    set_code='Promo_SWSH',
    key='Promo_SWSH',
    regulation_mark='F',
)

card.extra_attributes['200790'] = {'type': 'string', 'value': 'SWSH227'}
