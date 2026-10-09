from spirit.game.data_utils import reprint, sibling_card
from spirit.game.attributes import Rarities

card = reprint(
    sibling_card(__file__, "../BW9/Exeggcute_4.py"),
    collector_number=102,
    set_code="BW10",
    key="BW10",
    guid="a0c73251-03d7-5750-9b82-f806ac3a4fa9",
    rarity=Rarities.RareSecret,
)
