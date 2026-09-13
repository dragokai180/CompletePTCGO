# Gallery print swsh12pt5gg/GG18; artwork is downloaded by the installer.
from spirit.game.scripts.cards.SWSH10.Magnezone_107 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=178,
    rarity=Rarities.ChrRareHolo,
    guid='2abf870a-e78c-5305-80b2-6ad5b5180c84',
    set_code='CZ',
    key='CZ',
    regulation_mark='F',
)

card.extra_attributes["200790"] = {"type": "string", "value": "GG18"}
