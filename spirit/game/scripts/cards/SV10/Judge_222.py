from spirit.game.data_utils import reprint, sibling_card
from spirit.game.attributes import Rarities

card = reprint(sibling_card(__file__, "Judge_167.py"),
               collector_number=222, rarity=Rarities.RareUltra,
               regulation_mark="G")
