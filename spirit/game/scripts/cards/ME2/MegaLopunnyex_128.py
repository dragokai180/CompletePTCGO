from spirit.game.data_utils import reprint, sibling_card
from spirit.game.attributes import Rarities

card = reprint(sibling_card(__file__, "MegaLopunnyex_84.py"),
               collector_number=128, rarity=Rarities.RareSecret,
               regulation_mark="I")
