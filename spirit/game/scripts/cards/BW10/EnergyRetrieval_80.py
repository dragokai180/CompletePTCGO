from spirit.game.data_utils import reprint, sibling_card
from spirit.game.attributes import Rarities

card = reprint(
    sibling_card(__file__, "../CZ/EnergyRetrieval_127.py"),
    collector_number=80,
    set_code="BW10",
    key="BW10",
    guid="ce769df0-6b2b-52e1-8901-644c4c43d1e4",
    rarity=Rarities.Uncommon,
)
