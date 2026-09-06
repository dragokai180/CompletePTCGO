from spirit.game.data_utils import reprint, sibling_card
from spirit.game.attributes import Rarities

card = reprint(sibling_card(__file__, "Cinccinoex_73.py"),
               collector_number=105, rarity=Rarities.RareUltra,
               regulation_mark="J")
