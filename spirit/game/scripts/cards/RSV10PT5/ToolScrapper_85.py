from spirit.game.data_utils import reprint, sibling_card
from spirit.game.attributes import Rarities

card = reprint(sibling_card(__file__, "../SWSH2/ToolScrapper_168.py"),
               collector_number=85, rarity=Rarities.Uncommon,
               set_code="RSV10PT5", key="RSV10PT5",
               regulation_mark="I")
