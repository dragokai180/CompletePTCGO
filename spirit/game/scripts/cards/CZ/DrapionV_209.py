# Gallery print swsh12pt5gg/GG49; artwork is downloaded by the installer.
from spirit.game.scripts.cards.SWSH11.DrapionV_118 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=209,
    rarity=Rarities.RareHoloV,
    guid='930da419-01d6-5f22-a77e-e81e209e8485',
    set_code='CZ',
    key='CZ',
    regulation_mark='F',
)

card.extra_attributes["200790"] = {"type": "string", "value": "GG49"}
