from spirit.game.data_utils import reprint, sibling_card
from spirit.game.attributes import Rarities

card = reprint(sibling_card(__file__, "Bastiodon_62.py"),
               collector_number=93, rarity=Rarities.RareUltra,
               regulation_mark="J")
