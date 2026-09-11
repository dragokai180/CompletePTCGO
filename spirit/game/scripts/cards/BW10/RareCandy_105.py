from spirit.game.data_utils import reprint, sibling_card
from spirit.game.attributes import Rarities

card = reprint(
    sibling_card(__file__, "RareCandy_85.py"),
    collector_number=105,
    guid="6a7bcfd6-023a-59bf-9932-9053b3d78b08",
    rarity=Rarities.RareSecret,
)
