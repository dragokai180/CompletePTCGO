from spirit.game.data_utils import reprint, sibling_card
from spirit.game.attributes import Rarities

card = reprint(sibling_card(__file__, "Carmine_145.py"),
               collector_number=217, rarity=Rarities.RareSecret,
               regulation_mark="H")
