from spirit.game.data_utils import reprint, sibling_card
from spirit.game.attributes import Rarities

card = reprint(sibling_card(__file__, "../SV08/ScrambleSwitch_186.py"),
               collector_number=129, rarity=Rarities.Ace,
               set_code="BW8", key="BW8")
