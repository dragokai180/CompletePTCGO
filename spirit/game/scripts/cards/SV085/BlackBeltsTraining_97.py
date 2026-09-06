from spirit.game.data_utils import reprint, sibling_card
from spirit.game.attributes import Rarities

card = reprint(sibling_card(__file__, "BlackBeltsTraining_96.py"),
               collector_number=97, rarity=Rarities.Common,
               regulation_mark="H")
