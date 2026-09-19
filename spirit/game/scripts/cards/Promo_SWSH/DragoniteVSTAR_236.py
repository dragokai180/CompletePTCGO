from spirit.game.scripts.cards.PGO.DragoniteVSTAR_50 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=236,
    rarity=Rarities.RarePromo,
    guid='2bd92ef3-302a-5c8f-98d0-8e1f2ff335a0',
    set_code='Promo_SWSH',
    key='Promo_SWSH',
    regulation_mark='F',
)

card.extra_attributes['200790'] = {'type': 'string', 'value': 'SWSH236'}
