from spirit.game.data_utils import reprint, sibling_card
from spirit.game.attributes import Rarities

card = reprint(sibling_card(__file__, "../SV06/Munkidori_95.py"),
               collector_number=44, rarity=Rarities.Rare,
               set_code="SV085", key="SV085",
               regulation_mark="H")
