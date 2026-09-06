from spirit.game.data_utils import reprint, sibling_card
from spirit.game.attributes import Rarities

card = reprint(sibling_card(__file__, "../CZ/EnergySearch_128.py"),
               collector_number=72, rarity=Rarities.Common,
               set_code="ME3", key="ME3",
               regulation_mark="J")
