from spirit.game.data_utils import reprint, sibling_card
from spirit.game.attributes import Rarities

card = reprint(sibling_card(__file__, "Briar_132.py"),
               collector_number=171, rarity=Rarities.RareSecret,
               regulation_mark="H")
