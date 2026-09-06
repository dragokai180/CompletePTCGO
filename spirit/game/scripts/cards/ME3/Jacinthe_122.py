from spirit.game.data_utils import reprint, sibling_card
from spirit.game.attributes import Rarities

card = reprint(sibling_card(__file__, "Jacinthe_75.py"),
               collector_number=122, rarity=Rarities.RareSecret,
               regulation_mark="J")
