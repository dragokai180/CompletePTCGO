from spirit.game.data_utils import reprint, sibling_card
from spirit.game.attributes import Rarities

card = reprint(sibling_card(__file__, "Kieran_154.py"),
               collector_number=218, rarity=Rarities.RareSecret,
               regulation_mark="H")
