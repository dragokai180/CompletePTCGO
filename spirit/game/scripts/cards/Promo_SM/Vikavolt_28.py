from spirit.game.scripts.cards.SM1.Vikavolt_52 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=28,
    rarity=Rarities.RarePromo,
    guid='5a427e0f-e3b5-5b44-8e93-262725c24d27',
    set_code='Promo_SM',
    key='Promo_SM',
    regulation_mark=None,
)
