from spirit.game.data_utils import reprint, sibling_card
from spirit.game.attributes import Rarities

card = reprint(sibling_card(__file__, "../ME2/MegaDiancieex_41.py"),
               collector_number=267, rarity=Rarities.Rare,
               set_code="ME2PT5", key="ME2PT5",
               regulation_mark="I")
