# Gallery print swsh12pt5gg/GG69; artwork is downloaded by the installer.
from spirit.game.scripts.cards.SWSH11.GiratinaVSTAR_131 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=229,
    rarity=Rarities.RareSecret,
    guid='5bb2595e-f648-5396-b2c0-d1b63316590d',
    set_code='CZ',
    key='CZ',
    regulation_mark='F',
)

card.extra_attributes["200790"] = {"type": "string", "value": "GG69"}
