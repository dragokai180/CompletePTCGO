from spirit.game.data_utils import reprint, sibling_card
from spirit.game.attributes import Rarities

card = reprint(sibling_card(__file__, "../ME1/PremiumPowerPro_124.py"),
               collector_number=199, rarity=Rarities.Uncommon,
               set_code="ME2PT5", key="ME2PT5",
               regulation_mark="I")
