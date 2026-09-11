from spirit.game.data_utils import reprint, sibling_card
from spirit.game.attributes import Rarities

card = reprint(sibling_card(__file__, "../SWSH2/ToolScrapper_168.py"),
               collector_number=116, rarity=Rarities.Uncommon,
               set_code="BW6", key="BW6")
