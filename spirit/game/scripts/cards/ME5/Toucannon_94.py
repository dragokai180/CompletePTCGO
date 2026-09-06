from spirit.game.data_utils import reprint, sibling_card
from spirit.game.attributes import Rarities

card = reprint(sibling_card(__file__, "Toucannon_68.py"),
               collector_number=94, rarity=Rarities.RareUltra,
               regulation_mark="J")
