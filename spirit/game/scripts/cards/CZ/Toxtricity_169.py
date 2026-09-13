# Gallery print swsh12pt5gg/GG09; artwork is downloaded by the installer.
from spirit.game.scripts.cards.SWSH8.Toxtricity_108 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=169,
    rarity=Rarities.ChrRareHolo,
    guid='c29b6903-44bf-5577-8fb6-2ba3e6a64cce',
    set_code='CZ',
    key='CZ',
    regulation_mark='E',
)

card.extra_attributes["200790"] = {"type": "string", "value": "GG09"}
