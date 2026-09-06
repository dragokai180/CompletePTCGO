from spirit.game.data_utils import reprint, sibling_card
from spirit.game.attributes import Rarities

card = reprint(sibling_card(__file__, "../SWSH2/ToolScrapper_168.py"),
               collector_number=115, rarity=Rarities.RareUltra,
               set_code="ME4", key="ME4",
               regulation_mark="I")
