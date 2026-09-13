# Gallery print swsh12pt5gg/GG60; artwork is downloaded by the installer.
from spirit.game.scripts.cards.SWSH9.CynthiasAmbition_138 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=220,
    rarity=Rarities.RareUltra,
    guid='4ce75eab-b578-578b-b13c-26721eb57e56',
    set_code='CZ',
    key='CZ',
    regulation_mark='F',
)

card.extra_attributes["200790"] = {"type": "string", "value": "GG60"}
