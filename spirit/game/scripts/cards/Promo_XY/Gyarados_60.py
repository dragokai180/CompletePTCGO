from spirit.game.scripts.cards.XY7.Gyarados_21 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=60,
    rarity=Rarities.RarePromo,
    guid='14c436c2-3657-5cb6-88d5-b7e1b9479496',
    set_code='Promo_XY',
    key='Promo_XY',
    regulation_mark=None,
)
