from spirit.game.data_utils import reprint, sibling_card
from spirit.game.attributes import Rarities

card = reprint(
    sibling_card(__file__, "Iris_81.py"),
    collector_number=101,
    guid="ea50251c-acc9-52a9-b08a-ed69e761b704",
    rarity=Rarities.RareUltra,
)
