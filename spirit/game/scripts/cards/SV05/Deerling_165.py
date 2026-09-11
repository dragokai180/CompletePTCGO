from spirit.game.scripts.cards.SV05.Deerling_16 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=165,
    rarity=Rarities.ChrRareHolo,
    guid="0c5cc0b0-b888-5c1f-954e-bf9ddb0aefba",
    set_code="SV05",
    key="SV05",
    regulation_mark="H",
)
