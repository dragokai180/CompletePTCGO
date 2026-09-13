# Gallery print swsh12pt5gg/GG02; artwork is downloaded by the installer.
from spirit.game.scripts.cards.SWSH10.Kricketune_10 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=162,
    rarity=Rarities.ChrRareHolo,
    guid='a61b5848-8463-5098-9e9c-0e1fc9052aab',
    set_code='CZ',
    key='CZ',
    regulation_mark='F',
)

card.extra_attributes["200790"] = {"type": "string", "value": "GG02"}
