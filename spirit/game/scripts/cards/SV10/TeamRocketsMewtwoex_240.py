from spirit.game.data_utils import reprint, sibling_card
from spirit.game.attributes import Rarities

card = reprint(sibling_card(__file__, "TeamRocketsMewtwoex_81.py"),
               collector_number=240, rarity=Rarities.RareSecret,
               regulation_mark="I")
