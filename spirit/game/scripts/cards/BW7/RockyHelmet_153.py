from spirit.game.data_utils import reprint, sibling_card
from spirit.game.attributes import Rarities

card = reprint(sibling_card(__file__, "../SWSH4/RockyHelmet_159.py"),
               collector_number=153, rarity=Rarities.RareSecret,
               set_code="BW7", key="BW7")
