from spirit.game.data_utils import reprint, sibling_card
from spirit.game.attributes import Rarities

card = reprint(sibling_card(__file__, "../SV06/WellspringMaskOgerponex_64.py"),
               collector_number=27, rarity=Rarities.RareHoloEX,
               set_code="SV085", key="SV085",
               regulation_mark="H")
