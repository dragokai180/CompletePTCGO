"""Full-art reprint of Iron Leaves ex (TEF 186). Mechanics live in IronLeavesex_25."""
from spirit.game.attributes import Rarities
from spirit.game.data_utils import reprint, sibling_card

card = reprint(
    sibling_card(__file__, "IronLeavesex_25.py"),
    collector_number=186,
    rarity=Rarities.RareUltra,
)
