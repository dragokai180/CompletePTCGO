from spirit.game.data_utils import reprint, sibling_card
from spirit.game.attributes import Rarities

card = reprint(sibling_card(__file__, "Meowthex_62.py"),
               collector_number=121, rarity=Rarities.RareSecret,
               regulation_mark="J")
