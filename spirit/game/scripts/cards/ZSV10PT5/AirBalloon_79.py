from spirit.game.data_utils import reprint, sibling_card
from spirit.game.attributes import Rarities

card = reprint(sibling_card(__file__, "../SWSH1/AirBalloon_156.py"),
               collector_number=79, rarity=Rarities.Uncommon,
               set_code="ZSV10PT5", key="ZSV10PT5",
               regulation_mark="I")
