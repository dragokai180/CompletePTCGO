from spirit.game.scripts.cards.CZ.LeafeonVSTAR_14 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=195,
    rarity=Rarities.RarePromo,
    guid='32ec7e77-09d5-5141-b008-869dba9cf481',
    set_code='Promo_SWSH',
    key='Promo_SWSH',
    regulation_mark='F',
)

card.extra_attributes['200790'] = {'type': 'string', 'value': 'SWSH195'}
