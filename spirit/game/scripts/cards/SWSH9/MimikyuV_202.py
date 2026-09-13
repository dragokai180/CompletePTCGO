# Gallery print swsh9tg/TG16; artwork is downloaded by the installer.
from spirit.game.scripts.cards.SWSH5.MimikyuV_62 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=202,
    rarity=Rarities.RareHoloV,
    guid='a361563e-9324-5425-a14c-52a7ec10fab4',
    set_code='SWSH9',
    key='SWSH9',
    regulation_mark='E',
)

card.extra_attributes["200790"] = {"type": "string", "value": "TG16"}
