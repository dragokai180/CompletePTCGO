from spirit.game.data_utils import reprint, sibling_card
from spirit.game.attributes import Rarities

card = reprint(sibling_card(__file__, "LegendaryOceanTrench_71.py"),
               collector_number=72, rarity=Rarities.Uncommon,
               regulation_mark="J")
