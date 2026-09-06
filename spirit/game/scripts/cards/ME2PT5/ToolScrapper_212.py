from spirit.game.data_utils import reprint, sibling_card
from spirit.game.attributes import Rarities

card = reprint(sibling_card(__file__, "../SWSH2/ToolScrapper_168.py"),
               collector_number=212, rarity=Rarities.Common,
               set_code="ME2PT5", key="ME2PT5",
               regulation_mark="I")
