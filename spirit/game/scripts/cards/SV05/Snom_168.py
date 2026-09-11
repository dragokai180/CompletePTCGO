from spirit.game.scripts.cards.SV05.Snom_45 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=168,
    rarity=Rarities.ChrRareHolo,
    guid="02e8594c-abf9-5f75-9191-3d731a2739c4",
    set_code="SV05",
    key="SV05",
    regulation_mark="H",
)
