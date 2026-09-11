from spirit.game.data_utils import reprint, sibling_card
from spirit.game.attributes import Rarities

card = reprint(sibling_card(__file__, "../BW3/SuperRod_95.py"),
               collector_number=20, rarity=Rarities.RareHolo,
               set_code="DV", key="DV")
