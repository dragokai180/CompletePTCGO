# Gallery print swsh12pt5gg/GG39; artwork is downloaded by the installer.
from spirit.game.scripts.cards.SWSH9.LumineonV_40 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=199,
    rarity=Rarities.RareHoloV,
    guid='4a32bc00-42cc-5159-8660-de94adb445f0',
    set_code='CZ',
    key='CZ',
    regulation_mark='F',
)

card.extra_attributes["200790"] = {"type": "string", "value": "GG39"}
