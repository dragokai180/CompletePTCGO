from spirit.game.scripts.cards.ME2.Ludicolo_7 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=95,
    rarity=Rarities.ChrRareHolo,
    guid="244d43ae-3d37-5c1f-9279-33b578238a65",
    set_code="ME2",
    key="ME2",
    regulation_mark="I",
)
