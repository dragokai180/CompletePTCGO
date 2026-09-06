from spirit.game.data_utils import reprint, sibling_card
from spirit.game.attributes import Rarities

card = reprint(sibling_card(__file__, "MegaEelektrossex_61.py"),
               collector_number=266, rarity=Rarities.Rare,
               regulation_mark="I")
