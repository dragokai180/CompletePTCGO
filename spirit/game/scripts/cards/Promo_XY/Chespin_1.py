from spirit.game.scripts.cards.XY0.Chespin_3 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=1,
    rarity=Rarities.RarePromo,
    guid='8c80a61a-fb35-5822-919d-8e9b44b37b7f',
    set_code='Promo_XY',
    key='Promo_XY',
    regulation_mark=None,
)
