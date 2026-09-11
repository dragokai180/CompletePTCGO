from spirit.game.data_utils import reprint, sibling_card
from spirit.game.attributes import Rarities

card = reprint(sibling_card(__file__, "../SWSH5/ExpShare_126.py"),
               collector_number=18, rarity=Rarities.Common,
               set_code="DV", key="DV")
