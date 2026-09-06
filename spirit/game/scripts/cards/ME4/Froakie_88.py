from spirit.game.data_utils import reprint, sibling_card
from spirit.game.attributes import Rarities

card = reprint(sibling_card(__file__, "Froakie_20.py"),
               collector_number=88, rarity=Rarities.RareUltra,
               regulation_mark="J")
