from spirit.game.data_utils import reprint, sibling_card
from spirit.game.attributes import Rarities

card = reprint(sibling_card(__file__, "../CZ/CrushingHammer_125.py"),
               collector_number=111, rarity=Rarities.Uncommon,
               set_code="BW11", key="BW11")
