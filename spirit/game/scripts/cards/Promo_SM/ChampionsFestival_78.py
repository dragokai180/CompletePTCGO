from spirit.game.scripts.cards.PROMO_BW.ChampionsFestival_BW95 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=78,
    rarity=Rarities.RarePromo,
    guid='0e80c2d3-ba27-54e5-87f0-fe658fe26278',
    set_code='Promo_SM',
    key='Promo_SM',
    regulation_mark=None,
)
