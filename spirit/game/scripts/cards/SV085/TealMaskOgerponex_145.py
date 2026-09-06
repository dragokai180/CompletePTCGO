from spirit.game.data_utils import reprint, sibling_card
from spirit.game.attributes import Rarities

card = reprint(sibling_card(__file__, "../SV06/TealMaskOgerponex_25.py"),
               collector_number=145, rarity=Rarities.RareSecret,
               set_code="SV085", key="SV085",
               regulation_mark="H")
