from spirit.game.data_utils import reprint, sibling_card
from spirit.game.attributes import Rarities

card = reprint(sibling_card(__file__, "RagingBoltex_123.py"),
               collector_number=196, rarity=Rarities.RareUltra,
               regulation_mark="H")
