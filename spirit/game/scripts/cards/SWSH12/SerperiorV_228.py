# Gallery print swsh12tg/TG13; artwork is downloaded by the installer.
from spirit.game.scripts.cards.SWSH12.SerperiorV_7 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=228,
    rarity=Rarities.RareHoloV,
    guid='7aba9597-78bc-5b20-a354-6ac74d5ca20f',
    set_code='SWSH12',
    key='SWSH12',
    regulation_mark='F',
)

card.extra_attributes["200790"] = {"type": "string", "value": "TG13"}
