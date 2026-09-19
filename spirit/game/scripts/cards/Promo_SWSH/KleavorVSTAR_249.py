from spirit.game.scripts.cards.SWSH10.KleavorVSTAR_196 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=249,
    rarity=Rarities.RarePromo,
    guid='45245d9e-0763-5f35-9a8a-45bc277b21e8',
    set_code='Promo_SWSH',
    key='Promo_SWSH',
    regulation_mark='F',
)

card.extra_attributes['200790'] = {'type': 'string', 'value': 'SWSH249'}
