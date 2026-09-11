from spirit.game.scripts.cards.SM12.RedBlue_202 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=234,
    rarity=Rarities.RareUltra,
    guid='42a54f77-ffd1-51ac-8175-70de265f2b2c',
    set_code='SM12',
    key='SM12',
    regulation_mark=None,
)
