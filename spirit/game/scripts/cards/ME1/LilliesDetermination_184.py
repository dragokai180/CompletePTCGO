from spirit.game.data_utils import reprint, sibling_card
from spirit.game.attributes import Rarities

card = reprint(sibling_card(__file__, "LilliesDetermination_119.py"),
               collector_number=184, rarity=Rarities.RareSecret,
               regulation_mark="I")
