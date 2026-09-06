from spirit.game.data_utils import reprint, sibling_card
from spirit.game.attributes import Rarities

card = reprint(sibling_card(__file__, "../SV08/Eevee_143.py"),
               collector_number=74, rarity=Rarities.Common,
               set_code="SV085", key="SV085",
               regulation_mark="H")
