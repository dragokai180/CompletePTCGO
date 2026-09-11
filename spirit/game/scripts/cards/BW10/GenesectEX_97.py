from spirit.game.data_utils import reprint, sibling_card
from spirit.game.attributes import Rarities

card = reprint(
    sibling_card(__file__, "GenesectEX_11.py"),
    collector_number=97,
    guid="501e6a72-3eff-500c-b5f4-7d5b8c03d3a4",
    rarity=Rarities.RareUltra,
)
