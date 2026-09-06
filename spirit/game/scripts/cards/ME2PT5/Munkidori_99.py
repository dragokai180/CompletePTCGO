from spirit.game.data_utils import reprint, sibling_card
from spirit.game.attributes import Rarities

card = reprint(sibling_card(__file__, "../SV06/Munkidori_95.py"),
               collector_number=99, rarity=Rarities.Rare,
               set_code="ME2PT5", key="ME2PT5",
               regulation_mark="H")
