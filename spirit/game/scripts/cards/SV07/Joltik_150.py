from spirit.game.scripts.cards.SV07.Joltik_50 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=150,
    rarity=Rarities.ChrRareHolo,
    guid="b0584275-e86c-5807-9b51-226012900909",
    set_code="SV07",
    key="SV07",
    regulation_mark="H",
)
