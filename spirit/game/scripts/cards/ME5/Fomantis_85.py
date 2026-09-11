from spirit.game.scripts.cards.ME5.Fomantis_3 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=85,
    rarity=Rarities.ChrRareHolo,
    guid="50c2ef1d-52e1-5e92-8aa6-7d3f38628052",
    set_code="ME5",
    key="ME5",
    regulation_mark="J",
)
