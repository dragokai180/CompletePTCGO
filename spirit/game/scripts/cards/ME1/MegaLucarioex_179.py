from spirit.game.data_utils import reprint, sibling_card
from spirit.game.attributes import Rarities

card = reprint(sibling_card(__file__, "MegaLucarioex_77.py"),
               collector_number=179, rarity=Rarities.RareSecret,
               regulation_mark="I")
