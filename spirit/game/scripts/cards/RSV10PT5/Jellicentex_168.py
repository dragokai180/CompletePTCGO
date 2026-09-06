from spirit.game.data_utils import reprint, sibling_card
from spirit.game.attributes import Rarities

card = reprint(sibling_card(__file__, "Jellicentex_45.py"),
               collector_number=168, rarity=Rarities.RareSecret,
               regulation_mark="I")
