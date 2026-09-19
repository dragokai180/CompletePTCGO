from spirit.game.scripts.cards.SWSH11.HisuianZoroarkV_146 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=297,
    rarity=Rarities.RarePromo,
    guid='f09ec70b-933b-5ca1-9239-2dc058692998',
    set_code='Promo_SWSH',
    key='Promo_SWSH',
    regulation_mark='F',
)

card.extra_attributes['200790'] = {'type': 'string', 'value': 'SWSH297'}
