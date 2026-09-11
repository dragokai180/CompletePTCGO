from spirit.game.data_utils import reprint, sibling_card
from spirit.game.attributes import Rarities

card = reprint(
    sibling_card(__file__, "../CZ/RareCandy_141.py"),
    collector_number=85,
    set_code="BW10",
    key="BW10",
    guid="330b636a-d948-5b62-af0c-1814e0ababca",
    rarity=Rarities.Uncommon,
)
