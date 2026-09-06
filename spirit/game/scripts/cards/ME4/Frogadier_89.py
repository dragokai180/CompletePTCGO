from spirit.game.data_utils import reprint, sibling_card
from spirit.game.attributes import Rarities

card = reprint(sibling_card(__file__, "Frogadier_21.py"),
               collector_number=89, rarity=Rarities.RareUltra,
               regulation_mark="J")
