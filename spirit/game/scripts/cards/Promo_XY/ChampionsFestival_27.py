from spirit.game.scripts.cards.PROMO_BW.ChampionsFestival_BW95 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=27,
    rarity=Rarities.RarePromo,
    guid='18518adf-4894-548f-a27b-78bb7783abdf',
    set_code='Promo_XY',
    key='Promo_XY',
    regulation_mark=None,
)
