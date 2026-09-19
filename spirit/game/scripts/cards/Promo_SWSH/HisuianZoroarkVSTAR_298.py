from spirit.game.scripts.cards.SWSH11.HisuianZoroarkVSTAR_147 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=298,
    rarity=Rarities.RarePromo,
    guid='128d0e9f-cfcf-55ea-aafb-c2c367eea7da',
    set_code='Promo_SWSH',
    key='Promo_SWSH',
    regulation_mark='F',
)

card.extra_attributes['200790'] = {'type': 'string', 'value': 'SWSH298'}
