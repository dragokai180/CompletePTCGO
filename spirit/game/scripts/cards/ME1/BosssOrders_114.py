from spirit.game.data_utils import reprint, sibling_card
from spirit.game.attributes import Rarities

card = reprint(sibling_card(__file__, "../SWSH2/BosssOrders_154.py"),
               collector_number=114, rarity=Rarities.Uncommon,
               set_code="ME1", key="ME1",
               regulation_mark="I")
