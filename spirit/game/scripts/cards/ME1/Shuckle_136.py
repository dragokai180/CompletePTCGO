from spirit.game.data_utils import reprint, sibling_card
from spirit.game.attributes import Rarities

card = reprint(sibling_card(__file__, "Shuckle_11.py"),
               collector_number=136, rarity=Rarities.RareUltra,
               regulation_mark="I")
