from spirit.game.data_utils import reprint, sibling_card
from spirit.game.attributes import Rarities

card = reprint(sibling_card(__file__, "../SV05/BuddyBuddyPoffin_144.py"),
               collector_number=223, rarity=Rarities.RareSecret,
               set_code="SV06", key="SV06",
               regulation_mark="H")
