# Gallery print swsh12tg/TG17; artwork is downloaded by the installer.
from spirit.game.scripts.cards.SWSH12.MawileV_70 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=232,
    rarity=Rarities.RareHoloV,
    guid='190b7a2f-b33d-587c-8c1b-7d589606c432',
    set_code='SWSH12',
    key='SWSH12',
    regulation_mark='F',
)

card.extra_attributes["200790"] = {"type": "string", "value": "TG17"}
