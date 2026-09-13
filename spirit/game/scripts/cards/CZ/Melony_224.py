# Gallery print swsh12pt5gg/GG64; artwork is downloaded by the installer.
from spirit.game.scripts.cards.SWSH6.Melony_146 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=224,
    rarity=Rarities.RareUltra,
    guid='92e2d6bb-7c7c-5372-aedb-487a623a1d5e',
    set_code='CZ',
    key='CZ',
    regulation_mark='E',
)

card.extra_attributes["200790"] = {"type": "string", "value": "GG64"}
