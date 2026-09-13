# Gallery print swsh9tg/TG22; artwork is downloaded by the installer.
from spirit.game.scripts.cards.SWSH7.UmbreonV_94 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=208,
    rarity=Rarities.RareHoloV,
    guid='5c00a7af-58a5-5fff-b85a-7c4ca02f3ce7',
    set_code='SWSH9',
    key='SWSH9',
    regulation_mark='E',
)

card.extra_attributes["200790"] = {"type": "string", "value": "TG22"}
