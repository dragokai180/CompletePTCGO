from spirit.game.data_utils import reprint, sibling_card
from spirit.game.attributes import Rarities

card = reprint(sibling_card(__file__, "SpikyEnergy_159.py"),
               collector_number=190, rarity=Rarities.RareSecret,
               regulation_mark="I")
