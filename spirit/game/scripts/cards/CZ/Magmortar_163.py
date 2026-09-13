# Gallery print swsh12pt5gg/GG03; artwork is downloaded by the installer.
from spirit.game.scripts.cards.SWSH9.Magmortar_20 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=163,
    rarity=Rarities.ChrRareHolo,
    guid='472d6ade-07db-5c2f-94c8-639266449c45',
    set_code='CZ',
    key='CZ',
    regulation_mark='F',
)

card.extra_attributes["200790"] = {"type": "string", "value": "GG03"}
