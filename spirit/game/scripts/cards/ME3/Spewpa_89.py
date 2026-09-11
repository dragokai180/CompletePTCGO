from spirit.game.scripts.cards.ME3.Spewpa_8 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=89,
    rarity=Rarities.ChrRareHolo,
    guid="04594f44-b555-540f-921d-f621f6330e32",
    set_code="ME3",
    key="ME3",
    regulation_mark="J",
)
