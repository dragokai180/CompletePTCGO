from spirit.game.data_utils import reprint, sibling_card
from spirit.game.attributes import Rarities

card = reprint(sibling_card(__file__, "RosasEncouragement_84.py"),
               collector_number=123, rarity=Rarities.RareSecret,
               regulation_mark="J")
