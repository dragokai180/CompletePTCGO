from spirit.game.data_utils import reprint, sibling_card
from spirit.game.attributes import Rarities

card = reprint(sibling_card(__file__, "Crustle_12.py"),
               collector_number=186, rarity=Rarities.RareUltra,
               regulation_mark="I")
