# Gallery print swsh12pt5gg/GG36; artwork is downloaded by the installer.
from spirit.game.scripts.cards.SWSH9.EnteiV_22 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=196,
    rarity=Rarities.RareHoloV,
    guid='6e6bbd53-859e-5c10-b5fa-a03473a109d3',
    set_code='CZ',
    key='CZ',
    regulation_mark='F',
)

card.extra_attributes["200790"] = {"type": "string", "value": "GG36"}
