from spirit.game.scripts.cards.SM1.Litten_24 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=23,
    rarity=Rarities.RarePromo,
    guid='03c436c6-9413-57d8-a655-8c6d422d398d',
    set_code='Promo_SM',
    key='Promo_SM',
    regulation_mark=None,
)
