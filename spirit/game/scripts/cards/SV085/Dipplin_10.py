from spirit.game.scripts.cards.SV06.Dipplin_18 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=10,
    rarity=Rarities.Uncommon,
    guid="e0caecc8-6e6e-5d17-84d0-9edfb4f5719e",
    set_code="SV085",
    key="SV085",
    regulation_mark="H",
)
