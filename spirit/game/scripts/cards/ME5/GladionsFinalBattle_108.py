from spirit.game.data_utils import reprint, sibling_card
from spirit.game.attributes import Rarities

card = reprint(sibling_card(__file__, "GladionsFinalBattle_77.py"),
               collector_number=108, rarity=Rarities.RareUltra,
               regulation_mark="J")
