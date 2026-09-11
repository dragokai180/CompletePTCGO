from spirit.game.data_utils import reprint, sibling_card
from spirit.game.attributes import Rarities

card = reprint(sibling_card(__file__, "../XY8/FloatStone_137.py"),
               collector_number=99, rarity=Rarities.Uncommon,
               set_code="BW9", key="BW9")
