# Gallery print swsh9tg/TG17; artwork is downloaded by the installer.
from spirit.game.scripts.cards.SWSH9.MimikyuVMAX_69 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=203,
    rarity=Rarities.RareHoloVMAX,
    guid='c589b235-5c47-55ce-940c-b4a8181eaa72',
    set_code='SWSH9',
    key='SWSH9',
    regulation_mark='E',
)

card.extra_attributes["200790"] = {"type": "string", "value": "TG17"}
