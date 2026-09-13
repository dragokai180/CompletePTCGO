# Gallery print swsh11tg/TG14; artwork is downloaded by the installer.
from spirit.game.scripts.cards.SWSH3.CentiskorchV_33 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=231,
    rarity=Rarities.RareHoloV,
    guid='f1a3c144-d317-5a5b-a7ad-cfb5ea7278f9',
    set_code='SWSH11',
    key='SWSH11',
    regulation_mark='D',
)

card.extra_attributes["200790"] = {"type": "string", "value": "TG14"}
