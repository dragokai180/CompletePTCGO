from spirit.game.data_utils import reprint, sibling_card
from spirit.game.attributes import Rarities

card = reprint(sibling_card(__file__, "../SV07/Terapagosex_128.py"),
               collector_number=169, rarity=Rarities.RareSecret,
               set_code="SV085", key="SV085",
               regulation_mark="H")
