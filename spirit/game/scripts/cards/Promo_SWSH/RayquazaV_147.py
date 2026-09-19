from spirit.game.scripts.cards.SWSH7.RayquazaV_110 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=147,
    rarity=Rarities.RarePromo,
    guid='3cc7afdc-b578-5e97-aa5f-bbae54757db2',
    set_code='Promo_SWSH',
    key='Promo_SWSH',
    regulation_mark='E',
)

card.extra_attributes['200790'] = {'type': 'string', 'value': 'SWSH147'}
