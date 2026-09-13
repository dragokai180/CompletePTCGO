# Gallery print swsh9tg/TG13; artwork is downloaded by the installer.
from spirit.game.scripts.cards.SWSH2.BoltundV_67 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=199,
    rarity=Rarities.RareHoloV,
    guid='5bf8fae9-5598-51dc-bb62-91b23f6dcb7a',
    set_code='SWSH9',
    key='SWSH9',
    regulation_mark='D',
)

card.extra_attributes["200790"] = {"type": "string", "value": "TG13"}
