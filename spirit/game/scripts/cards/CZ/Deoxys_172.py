# Gallery print swsh12pt5gg/GG12; artwork is downloaded by the installer.
from spirit.game.scripts.cards.SWSH8.Deoxys_120 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=172,
    rarity=Rarities.ChrRareHolo,
    guid='4c5c2ebe-7e18-5b1e-9057-0eab519c6c37',
    set_code='CZ',
    key='CZ',
    regulation_mark='E',
)

card.extra_attributes["200790"] = {"type": "string", "value": "GG12"}
