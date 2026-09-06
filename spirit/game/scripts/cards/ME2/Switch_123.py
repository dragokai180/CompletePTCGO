from spirit.game.data_utils import reprint, sibling_card
from spirit.game.attributes import Rarities

card = reprint(sibling_card(__file__, "../CZ/Switch_144.py"),
               collector_number=123, rarity=Rarities.RareUltra,
               set_code="ME2", key="ME2",
               regulation_mark="I")
