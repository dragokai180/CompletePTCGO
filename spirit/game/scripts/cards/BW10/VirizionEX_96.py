from spirit.game.data_utils import reprint, sibling_card
from spirit.game.attributes import Rarities

card = reprint(
    sibling_card(__file__, "VirizionEX_9.py"),
    collector_number=96,
    guid="5f7afba7-3ac5-5651-babb-752919414391",
    rarity=Rarities.RareUltra,
)
