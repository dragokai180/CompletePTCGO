from spirit.game.data_utils import reprint, sibling_card
from spirit.game.attributes import Rarities

card = reprint(sibling_card(__file__, "../SV10/TeamRocketsWatchtower_180.py"),
               collector_number=210, rarity=Rarities.Uncommon,
               set_code="ME2PT5", key="ME2PT5",
               regulation_mark="I")
