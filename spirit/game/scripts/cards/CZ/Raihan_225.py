# Gallery print swsh12pt5gg/GG65; artwork is downloaded by the installer.
from spirit.game.scripts.cards.SWSH7.Raihan_152 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=225,
    rarity=Rarities.RareUltra,
    guid='0fad0a99-a3af-588d-9dcc-58d22de2050f',
    set_code='CZ',
    key='CZ',
    regulation_mark='E',
)

card.extra_attributes["200790"] = {"type": "string", "value": "GG65"}
