from spirit.game.data_utils import reprint, sibling_card
from spirit.game.attributes import Rarities

card = reprint(sibling_card(__file__, "../SV05/MaximumBelt_154.py"),
               collector_number=117, rarity=Rarities.Ace,
               set_code="SV085", key="SV085",
               regulation_mark="H")
