from spirit.game.data_utils import reprint, sibling_card
from spirit.game.attributes import Rarities

card = reprint(sibling_card(__file__, "../SV09/LilliesClefairyex_56.py"),
               collector_number=280, rarity=Rarities.RareSecret,
               set_code="ME2PT5", key="ME2PT5",
               regulation_mark="I")
