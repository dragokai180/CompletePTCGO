from spirit.game.data_utils import reprint, sibling_card
from spirit.game.attributes import Rarities

card = reprint(sibling_card(__file__, "Crispin_133.py"),
               collector_number=164, rarity=Rarities.RareUltra,
               regulation_mark="H")
