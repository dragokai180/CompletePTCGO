# Gallery print swsh12pt5gg/GG31; artwork is downloaded by the installer.
from spirit.game.scripts.cards.SWSH9.Turtwig_6 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=191,
    rarity=Rarities.ChrRareHolo,
    guid='7d88d88c-643f-58e8-8117-9c898dc00be3',
    set_code='CZ',
    key='CZ',
    regulation_mark='F',
)

card.extra_attributes["200790"] = {"type": "string", "value": "GG31"}
