from spirit.game.scripts.cards.ME1.Steelix_93 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=150,
    rarity=Rarities.ChrRareHolo,
    guid="9a0b0ed7-41e6-56ca-b3e9-76a04ee0839e",
    set_code="ME1",
    key="ME1",
    regulation_mark="I",
)
