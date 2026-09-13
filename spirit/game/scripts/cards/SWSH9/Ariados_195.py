# Gallery print swsh9tg/TG09; artwork is downloaded by the installer.
from spirit.game.scripts.cards.SWSH3.Ariados_103 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=195,
    rarity=Rarities.ChrRareHolo,
    guid='86744baf-3b8e-58d3-9e9e-361b7057c32b',
    set_code='SWSH9',
    key='SWSH9',
    regulation_mark='D',
)

card.extra_attributes["200790"] = {"type": "string", "value": "TG09"}
