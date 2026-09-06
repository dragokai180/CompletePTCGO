from spirit.game.data_utils import reprint, sibling_card
from spirit.game.attributes import Rarities

card = reprint(sibling_card(__file__, "BattleCage_85.py"),
               collector_number=116, rarity=Rarities.RareUltra,
               regulation_mark="I")
