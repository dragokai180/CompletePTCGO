from spirit.game.data_utils import reprint, sibling_card
from spirit.game.attributes import Rarities

card = reprint(
    sibling_card(__file__, "DialgaEX_65.py"),
    collector_number=99,
    guid="95fd495f-1f25-59e9-9e95-42229e5d14d1",
    rarity=Rarities.RareUltra,
)
