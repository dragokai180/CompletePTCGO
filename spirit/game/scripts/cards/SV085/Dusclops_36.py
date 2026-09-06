from spirit.game.data_utils import reprint, sibling_card
from spirit.game.attributes import Rarities

card = reprint(sibling_card(__file__, "../SV065/Dusclops_19.py"),
               collector_number=36, rarity=Rarities.Common,
               set_code="SV085", key="SV085",
               regulation_mark="H")
