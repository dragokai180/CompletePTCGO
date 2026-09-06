from spirit.game.data_utils import reprint, sibling_card
from spirit.game.attributes import Rarities

card = reprint(sibling_card(__file__, "Canari_185.py"),
               collector_number=257, rarity=Rarities.RareUltra,
               regulation_mark="I")
