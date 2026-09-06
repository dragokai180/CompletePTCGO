from spirit.game.data_utils import reprint, sibling_card
from spirit.game.attributes import Rarities

card = reprint(sibling_card(__file__, "MegaGreninjaex_22.py"),
               collector_number=122, rarity=Rarities.Rare,
               regulation_mark="J")
