from spirit.game.scripts.cards.SWSH10.HisuianDecidueyeV_83 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=238,
    rarity=Rarities.RarePromo,
    guid='4a4a6378-21c3-58a3-bd78-919006659ec1',
    set_code='Promo_SWSH',
    key='Promo_SWSH',
    regulation_mark='F',
)

card.extra_attributes['200790'] = {'type': 'string', 'value': 'SWSH238'}
