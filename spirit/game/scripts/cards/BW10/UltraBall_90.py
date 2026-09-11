from spirit.game.data_utils import reprint, sibling_card
from spirit.game.attributes import Rarities

card = reprint(
    sibling_card(__file__, "../CZ/UltraBall_146.py"),
    collector_number=90,
    set_code="BW10",
    key="BW10",
    guid="8a54334f-2780-514e-b8fd-bc3e4391839a",
    rarity=Rarities.Uncommon,
)
