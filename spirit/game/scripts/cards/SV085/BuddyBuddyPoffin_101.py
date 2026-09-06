from spirit.game.data_utils import reprint, sibling_card
from spirit.game.attributes import Rarities

card = reprint(sibling_card(__file__, "../SV05/BuddyBuddyPoffin_144.py"),
               collector_number=101, rarity=Rarities.Uncommon,
               set_code="SV085", key="SV085",
               regulation_mark="H")
