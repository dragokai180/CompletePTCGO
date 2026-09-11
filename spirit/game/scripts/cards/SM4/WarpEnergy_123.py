from spirit.game.scripts.cards.SL.WarpEnergy_70 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=123,
    rarity=Rarities.RareSecret,
    guid='a0cf3f3d-63c0-5396-bbaf-d1d4b1aa7ef6',
    set_code='SM4',
    key='SM4',
    regulation_mark=None,
)
