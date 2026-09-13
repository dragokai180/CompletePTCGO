# Gallery print swsh12pt5gg/GG23; artwork is downloaded by the installer.
from spirit.game.scripts.cards.SWSH8.Dunsparce_207 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=183,
    rarity=Rarities.ChrRareHolo,
    guid='de4904e0-f3a6-56b2-a6e9-53b32b2a66a6',
    set_code='CZ',
    key='CZ',
    regulation_mark='E',
)

card.extra_attributes["200790"] = {"type": "string", "value": "GG23"}
