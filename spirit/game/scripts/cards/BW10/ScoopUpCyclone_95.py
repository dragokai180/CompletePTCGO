from spirit.game.data_utils import reprint, sibling_card
from spirit.game.attributes import Rarities

card = reprint(
    sibling_card(__file__, "../SV06/ScoopUpCyclone_162.py"),
    collector_number=95,
    set_code="BW10",
    key="BW10",
    guid="ef31f3c0-8c03-5904-9a30-af0472e7a8d2",
    rarity=Rarities.Ace,
)
