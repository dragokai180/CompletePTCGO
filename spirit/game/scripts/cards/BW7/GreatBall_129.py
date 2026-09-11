from spirit.game.data_utils import reprint, sibling_card
from spirit.game.attributes import Rarities

card = reprint(sibling_card(__file__, "../CZ/GreatBall_132.py"),
               collector_number=129, rarity=Rarities.Uncommon,
               set_code="BW7", key="BW7")
