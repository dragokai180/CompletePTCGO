from spirit.game.scripts.cards.ME2.Flygon_53 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=101,
    rarity=Rarities.ChrRareHolo,
    guid="eb7c8647-707d-5cf1-b00f-25122d655476",
    set_code="ME2",
    key="ME2",
    regulation_mark="I",
)
