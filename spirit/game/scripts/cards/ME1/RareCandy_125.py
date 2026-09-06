from spirit.game.data_utils import reprint, sibling_card
from spirit.game.attributes import Rarities

card = reprint(sibling_card(__file__, "../CZ/RareCandy_141.py"),
               collector_number=125, rarity=Rarities.Common,
               set_code="ME1", key="ME1",
               regulation_mark="I")
