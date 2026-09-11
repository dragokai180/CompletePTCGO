from spirit.game.data_utils import reprint, sibling_card
from spirit.game.attributes import Rarities

card = reprint(
    sibling_card(__file__, "PalkiaEX_66.py"),
    collector_number=100,
    guid="33eaa38d-f7dd-52fa-a91c-5e1c7e384799",
    rarity=Rarities.RareUltra,
)
