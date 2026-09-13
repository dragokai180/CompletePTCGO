# Gallery print swsh12pt5gg/GG47; artwork is downloaded by the installer.
from spirit.game.scripts.cards.CZ.HattereneVMAX_66 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=207,
    rarity=Rarities.RareHoloVMAX,
    guid='7ab746c7-bec3-527f-9dbf-5572200495d5',
    set_code='CZ',
    key='CZ',
    regulation_mark='F',
)

card.extra_attributes["200790"] = {"type": "string", "value": "GG47"}
