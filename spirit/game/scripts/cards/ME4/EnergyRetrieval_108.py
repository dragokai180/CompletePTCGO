from spirit.game.data_utils import reprint, sibling_card
from spirit.game.attributes import Rarities

card = reprint(sibling_card(__file__, "../CZ/EnergyRetrieval_127.py"),
               collector_number=108, rarity=Rarities.RareUltra,
               set_code="ME4", key="ME4",
               regulation_mark="I")
