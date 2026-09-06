from spirit.game.data_utils import reprint, sibling_card
from spirit.game.attributes import Rarities

card = reprint(sibling_card(__file__, "../SV065/NightStretcher_61.py"),
               collector_number=251, rarity=Rarities.RareSecret,
               set_code="SV08", key="SV08",
               regulation_mark="H")
