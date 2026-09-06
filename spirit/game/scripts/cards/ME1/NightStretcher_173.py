from spirit.game.data_utils import reprint, sibling_card
from spirit.game.attributes import Rarities

card = reprint(sibling_card(__file__, "../SV065/NightStretcher_61.py"),
               collector_number=173, rarity=Rarities.RareUltra,
               set_code="ME1", key="ME1",
               regulation_mark="H")
