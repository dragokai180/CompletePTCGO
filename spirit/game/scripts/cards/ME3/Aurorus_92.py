from spirit.game.scripts.cards.ME3.Aurorus_24 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=92,
    rarity=Rarities.ChrRareHolo,
    guid="bc2fa664-857b-5177-b8b5-a26125fdd6f5",
    set_code="ME3",
    key="ME3",
    regulation_mark="J",
)
