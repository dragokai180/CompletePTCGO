from spirit.game.data_utils import reprint, sibling_card
from spirit.game.attributes import Rarities

card = reprint(sibling_card(__file__, "../SWSH5/LevelBall_129.py"),
               collector_number=89, rarity=Rarities.Uncommon,
               set_code="BW4", key="BW4")
