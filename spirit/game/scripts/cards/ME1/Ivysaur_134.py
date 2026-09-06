from spirit.game.data_utils import reprint, sibling_card
from spirit.game.attributes import Rarities

card = reprint(sibling_card(__file__, "Ivysaur_2.py"),
               collector_number=134, rarity=Rarities.RareUltra,
               regulation_mark="I")
