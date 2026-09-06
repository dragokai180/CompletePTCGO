from spirit.game.data_utils import reprint, sibling_card
from spirit.game.attributes import Rarities

card = reprint(sibling_card(__file__, "../SV06/JammingTower_153.py"),
               collector_number=243, rarity=Rarities.RareSecret,
               set_code="SV10", key="SV10",
               regulation_mark="H")
