from spirit.game.data_utils import reprint, sibling_card
from spirit.game.attributes import Rarities

card = reprint(sibling_card(__file__, "../SV05/Dunsparce_128.py"),
               collector_number=79, rarity=Rarities.Common,
               set_code="SV085", key="SV085",
               regulation_mark="H")
