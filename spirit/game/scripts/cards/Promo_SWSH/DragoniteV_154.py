from spirit.game.scripts.cards.SWSH7.DragoniteV_191 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=154,
    rarity=Rarities.RarePromo,
    guid='b6286cf8-cff3-5ae2-8de9-0348cb2529de',
    set_code='Promo_SWSH',
    key='Promo_SWSH',
    regulation_mark='E',
)

card.extra_attributes['200790'] = {'type': 'string', 'value': 'SWSH154'}
