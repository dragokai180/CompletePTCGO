from spirit.game.data_utils import reprint, sibling_card
from spirit.game.attributes import Rarities

card = reprint(sibling_card(__file__, "Frillish_44.py"),
               collector_number=126, rarity=Rarities.RareUltra,
               regulation_mark="I")
