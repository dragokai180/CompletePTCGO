from spirit.game.scripts.cards.Promo_SM.Pikachu_4 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=81,
    rarity=Rarities.RarePromo,
    guid='e55778c1-994c-5f78-8441-ad95e9243514',
    set_code='Promo_SM',
    key='Promo_SM',
    regulation_mark=None,
)
