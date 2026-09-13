# Gallery print swsh10tg/TG03; artwork is downloaded by the installer.
from spirit.game.scripts.cards.SWSH5.Kingdra_33 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=219,
    rarity=Rarities.ChrRareHolo,
    guid='d7799e20-ebf0-550a-b42a-6ee9f8ec28bc',
    set_code='SWSH10',
    key='SWSH10',
    regulation_mark='E',
)

card.extra_attributes["200790"] = {"type": "string", "value": "TG03"}
