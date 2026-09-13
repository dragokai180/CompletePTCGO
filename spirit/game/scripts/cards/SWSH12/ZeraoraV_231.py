# Gallery print swsh12tg/TG16; artwork is downloaded by the installer.
from spirit.game.scripts.cards.SWSH6.ZeraoraV_53 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=231,
    rarity=Rarities.RareHoloV,
    guid='6a6d0790-2741-5256-9caa-492776c8f810',
    set_code='SWSH12',
    key='SWSH12',
    regulation_mark='E',
)

card.extra_attributes["200790"] = {"type": "string", "value": "TG16"}
