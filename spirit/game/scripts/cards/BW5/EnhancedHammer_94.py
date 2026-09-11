from spirit.game.data_utils import reprint, sibling_card
from spirit.game.attributes import Rarities

card = reprint(sibling_card(__file__, "../SV06/EnhancedHammer_148.py"),
               collector_number=94, rarity=Rarities.Uncommon,
               set_code="BW5", key="BW5")
