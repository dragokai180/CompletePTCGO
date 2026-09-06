from spirit.game.data_utils import reprint, sibling_card
from spirit.game.attributes import Rarities

card = reprint(sibling_card(__file__, "TeamRocketsAriana_171.py"),
               collector_number=237, rarity=Rarities.RareSecret,
               regulation_mark="I")
