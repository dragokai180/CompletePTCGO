from spirit.game.data_utils import reprint, sibling_card
from spirit.game.attributes import Rarities

card = reprint(sibling_card(__file__, "TealMaskOgerponex_25.py"),
               collector_number=221, rarity=Rarities.RareSecret,
               regulation_mark="H")
