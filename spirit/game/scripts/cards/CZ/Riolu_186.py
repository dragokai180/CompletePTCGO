# Gallery print swsh12pt5gg/GG26; artwork is downloaded by the installer.
from spirit.game.scripts.cards.SWSH9.Riolu_78 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=186,
    rarity=Rarities.ChrRareHolo,
    guid='170ceb3d-c3b5-5f76-8b78-b06ece40f069',
    set_code='CZ',
    key='CZ',
    regulation_mark='F',
)

card.extra_attributes["200790"] = {"type": "string", "value": "GG26"}
