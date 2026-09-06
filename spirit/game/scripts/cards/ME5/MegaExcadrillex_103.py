from spirit.game.data_utils import reprint, sibling_card
from spirit.game.attributes import Rarities

card = reprint(sibling_card(__file__, "MegaExcadrillex_65.py"),
               collector_number=103, rarity=Rarities.RareUltra,
               regulation_mark="J")
