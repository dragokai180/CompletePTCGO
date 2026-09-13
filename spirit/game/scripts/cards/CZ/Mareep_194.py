# Gallery print swsh12pt5gg/GG34; artwork is downloaded by the installer.
from spirit.game.scripts.cards.SWSH7.Mareep_54 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=194,
    rarity=Rarities.ChrRareHolo,
    guid='a8030b00-835b-5de3-a596-346e73e3c04c',
    set_code='CZ',
    key='CZ',
    regulation_mark='E',
)

card.extra_attributes["200790"] = {"type": "string", "value": "GG34"}
