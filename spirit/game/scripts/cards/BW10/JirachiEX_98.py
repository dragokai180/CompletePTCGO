from spirit.game.data_utils import reprint, sibling_card
from spirit.game.attributes import Rarities

card = reprint(
    sibling_card(__file__, "JirachiEX_60.py"),
    collector_number=98,
    guid="8069e1c4-479b-5a90-83b5-fd82c4ccfbbe",
    rarity=Rarities.RareUltra,
)
