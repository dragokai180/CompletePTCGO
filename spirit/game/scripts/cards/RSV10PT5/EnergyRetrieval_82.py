from spirit.game.data_utils import reprint, sibling_card
from spirit.game.attributes import Rarities

card = reprint(sibling_card(__file__, "../CZ/EnergyRetrieval_127.py"),
               collector_number=82, rarity=Rarities.Uncommon,
               set_code="RSV10PT5", key="RSV10PT5",
               regulation_mark="I")
