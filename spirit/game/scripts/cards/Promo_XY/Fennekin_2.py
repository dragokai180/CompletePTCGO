from spirit.game.scripts.cards.XY0.Fennekin_8 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=2,
    rarity=Rarities.RarePromo,
    guid='83f0365c-7466-5f18-8a4b-83c0ee0f540e',
    set_code='Promo_XY',
    key='Promo_XY',
    regulation_mark=None,
)
