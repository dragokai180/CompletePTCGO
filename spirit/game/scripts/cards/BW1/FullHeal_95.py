from spirit.game.data_utils import reprint, sibling_card
from spirit.game.attributes import Rarities

card = reprint(sibling_card(__file__, "../SWSH2/FullHeal_159.py"),
               collector_number=95, rarity=Rarities.Uncommon,
               set_code="BW1", key="BW1")
