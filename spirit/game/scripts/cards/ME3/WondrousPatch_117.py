from spirit.game.data_utils import reprint, sibling_card
from spirit.game.attributes import Rarities

card = reprint(sibling_card(__file__, "../ME2/WondrousPatch_94.py"),
               collector_number=117, rarity=Rarities.RareUltra,
               set_code="ME3", key="ME3",
               regulation_mark="I")
