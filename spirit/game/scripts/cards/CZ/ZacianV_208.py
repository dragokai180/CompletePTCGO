# Gallery print swsh12pt5gg/GG48; artwork is downloaded by the installer.
from spirit.game.scripts.cards.CEL25.ZacianV_16 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=208,
    rarity=Rarities.RareHoloV,
    guid='ce3650cc-fa4e-56b5-9c30-0038c796df18',
    set_code='CZ',
    key='CZ',
    regulation_mark='E',
)

card.extra_attributes["200790"] = {"type": "string", "value": "GG48"}
