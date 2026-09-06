from spirit.game.data_utils import reprint, sibling_card
from spirit.game.attributes import Rarities

card = reprint(sibling_card(__file__, "../CZ/UltraBall_146.py"),
               collector_number=131, rarity=Rarities.Common,
               set_code="ME1", key="ME1",
               regulation_mark="I")
