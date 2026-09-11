from spirit.game.data_utils import reprint, sibling_card
from spirit.game.attributes import Rarities

card = reprint(sibling_card(__file__, "../SWSH5/EscapeRope_125.py"),
               collector_number=120, rarity=Rarities.Uncommon,
               set_code="BW8", key="BW8")
