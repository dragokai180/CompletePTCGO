from spirit.game.data_utils import reprint, sibling_card
from spirit.game.attributes import Rarities

card = reprint(sibling_card(__file__, "../CZ/EnergySearch_128.py"),
               collector_number=128, rarity=Rarities.Common,
               set_code="BW7", key="BW7")
