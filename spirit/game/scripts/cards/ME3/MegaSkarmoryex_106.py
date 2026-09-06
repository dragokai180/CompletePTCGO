from spirit.game.data_utils import reprint, sibling_card
from spirit.game.attributes import Rarities

card = reprint(sibling_card(__file__, "MegaSkarmoryex_55.py"),
               collector_number=106, rarity=Rarities.RareUltra,
               regulation_mark="J")
