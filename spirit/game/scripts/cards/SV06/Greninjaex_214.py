from spirit.game.data_utils import reprint, sibling_card
from spirit.game.attributes import Rarities

card = reprint(sibling_card(__file__, "Greninjaex_106.py"),
               collector_number=214, rarity=Rarities.RareSecret,
               regulation_mark="H")
