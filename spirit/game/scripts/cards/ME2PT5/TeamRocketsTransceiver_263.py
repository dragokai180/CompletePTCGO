from spirit.game.data_utils import reprint, sibling_card
from spirit.game.attributes import Rarities

card = reprint(sibling_card(__file__, "../SV10/TeamRocketsTransceiver_178.py"),
               collector_number=263, rarity=Rarities.RareUltra,
               set_code="ME2PT5", key="ME2PT5",
               regulation_mark="I")
