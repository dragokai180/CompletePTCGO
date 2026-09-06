from spirit.game.data_utils import reprint, sibling_card
from spirit.game.attributes import Rarities

card = reprint(sibling_card(__file__, "../SV08/Togetic_71.py"),
               collector_number=81, rarity=Rarities.Common,
               set_code="ME2PT5", key="ME2PT5",
               regulation_mark="H")
