# Gallery print swsh9tg/TG10; artwork is downloaded by the installer.
from spirit.game.scripts.cards.SWSH5.Houndoom_96 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=196,
    rarity=Rarities.ChrRareHolo,
    guid='f9e20389-3779-58cc-8bed-3bb7160af044',
    set_code='SWSH9',
    key='SWSH9',
    regulation_mark='E',
)

card.extra_attributes["200790"] = {"type": "string", "value": "TG10"}
