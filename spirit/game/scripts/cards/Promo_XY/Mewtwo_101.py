from spirit.game.scripts.cards.Promo_XY.Mewtwo_100 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=101,
    rarity=Rarities.RarePromo,
    guid='e781774a-30fd-5852-b195-53c69c1a0830',
    set_code='Promo_XY',
    key='Promo_XY',
    regulation_mark=None,
)
