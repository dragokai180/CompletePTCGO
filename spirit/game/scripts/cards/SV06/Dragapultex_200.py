from spirit.game.data_utils import reprint, sibling_card
from spirit.game.attributes import Rarities

card = reprint(sibling_card(__file__, "Dragapultex_130.py"),
               collector_number=200, rarity=Rarities.RareUltra,
               regulation_mark="H")
