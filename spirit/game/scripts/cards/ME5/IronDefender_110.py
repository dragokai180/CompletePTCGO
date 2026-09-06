from spirit.game.data_utils import reprint, sibling_card
from spirit.game.attributes import Rarities

card = reprint(sibling_card(__file__, "../ME1/IronDefender_118.py"),
               collector_number=110, rarity=Rarities.RareUltra,
               set_code="ME5", key="ME5",
               regulation_mark="I")
