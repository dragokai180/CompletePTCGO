from spirit.game.data_utils import reprint, sibling_card
from spirit.game.attributes import Rarities

card = reprint(sibling_card(__file__, "Latiasex_76.py"),
               collector_number=220, rarity=Rarities.RareUltra,
               regulation_mark="H")
