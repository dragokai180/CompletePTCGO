from spirit.game.data_utils import reprint, sibling_card
from spirit.game.attributes import Rarities

card = reprint(sibling_card(__file__, "../CZ/UltraBall_146.py"),
               collector_number=122, rarity=Rarities.RareSecret,
               set_code="BW9", key="BW9")
