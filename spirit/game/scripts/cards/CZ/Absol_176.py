# Gallery print swsh12pt5gg/GG16; artwork is downloaded by the installer.
from spirit.game.scripts.cards.SWSH10.Absol_97 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=176,
    rarity=Rarities.ChrRareHolo,
    guid='6bae8567-dbf7-5b9c-8666-3a644fa8ffc1',
    set_code='CZ',
    key='CZ',
    regulation_mark='F',
)

card.extra_attributes["200790"] = {"type": "string", "value": "GG16"}
