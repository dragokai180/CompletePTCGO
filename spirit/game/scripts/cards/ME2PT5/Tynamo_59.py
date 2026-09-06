from spirit.game.data_utils import reprint, sibling_card
from spirit.game.attributes import Rarities

card = reprint(sibling_card(__file__, "../ZSV10PT5/Tynamo_30.py"),
               collector_number=59, rarity=Rarities.Common,
               set_code="ME2PT5", key="ME2PT5",
               regulation_mark="I")
