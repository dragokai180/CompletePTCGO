from spirit.game.data_utils import reprint, sibling_card
from spirit.game.attributes import Rarities

card = reprint(sibling_card(__file__, "BloodmoonUrsalunaex_141.py"),
               collector_number=202, rarity=Rarities.RareSecret,
               regulation_mark="H")
