from spirit.game.data_utils import reprint, sibling_card
from spirit.game.attributes import Rarities

card = reprint(sibling_card(__file__, "../ME2PT5/PokPad_198.py"),
               collector_number=113, rarity=Rarities.RareUltra,
               set_code="ME3", key="ME3",
               regulation_mark="J")
