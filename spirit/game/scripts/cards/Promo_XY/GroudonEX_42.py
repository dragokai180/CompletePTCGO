from spirit.game.scripts.cards.XY5.GroudonEX_85 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=42,
    rarity=Rarities.RarePromo,
    guid='31956e9d-b098-5538-9019-60e0dedecd1a',
    set_code='Promo_XY',
    key='Promo_XY',
    regulation_mark=None,
)
