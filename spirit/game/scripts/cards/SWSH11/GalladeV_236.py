# Gallery print swsh11tg/TG19; artwork is downloaded by the installer.
from spirit.game.scripts.cards.SWSH11.GalladeV_181 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=236,
    rarity=Rarities.RareHoloV,
    guid='645d064d-75a0-59f9-bddf-a214a81bfb19',
    set_code='SWSH11',
    key='SWSH11',
    regulation_mark='F',
)

card.extra_attributes["200790"] = {"type": "string", "value": "TG19"}
