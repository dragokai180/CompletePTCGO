# Gallery print swsh11tg/TG16; artwork is downloaded by the installer.
from spirit.game.scripts.cards.SWSH4.PikachuV_43 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=233,
    rarity=Rarities.RareHoloV,
    guid='50a47df8-0bb9-5179-a786-ae2fa15a4bb8',
    set_code='SWSH11',
    key='SWSH11',
    regulation_mark='D',
)

card.extra_attributes["200790"] = {"type": "string", "value": "TG16"}
