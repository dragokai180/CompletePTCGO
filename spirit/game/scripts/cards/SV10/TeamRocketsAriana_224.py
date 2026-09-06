from spirit.game.data_utils import reprint, sibling_card
from spirit.game.attributes import Rarities

card = reprint(sibling_card(__file__, "TeamRocketsAriana_171.py"),
               collector_number=224, rarity=Rarities.RareUltra,
               regulation_mark="I")
