from spirit.game.scripts.cards.ME2.Yamper_30 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=99,
    rarity=Rarities.ChrRareHolo,
    guid="e2c07a05-5527-5030-ba1a-e2ff831dc8ff",
    set_code="ME2",
    key="ME2",
    regulation_mark="I",
)
