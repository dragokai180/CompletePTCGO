from spirit.game.data_utils import reprint, sibling_card
from spirit.game.attributes import Rarities

card = reprint(sibling_card(__file__, "../ME2/JumboIceCream_91.py"),
               collector_number=109, rarity=Rarities.RareUltra,
               set_code="ME4", key="ME4",
               regulation_mark="I")
