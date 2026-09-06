from spirit.game.data_utils import reprint, sibling_card
from spirit.game.attributes import Rarities

card = reprint(sibling_card(__file__, "../SV08/Togekiss_72.py"),
               collector_number=82, rarity=Rarities.Rare,
               set_code="ME2PT5", key="ME2PT5",
               regulation_mark="H")
