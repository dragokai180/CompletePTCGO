from spirit.game.data_utils import reprint, sibling_card
from spirit.game.attributes import Rarities

card = reprint(sibling_card(__file__, "MysteryGarden_122.py"),
               collector_number=172, rarity=Rarities.RareUltra,
               regulation_mark="I")
