# Gallery print swsh12pt5gg/GG24; artwork is downloaded by the installer.
from spirit.game.scripts.cards.SWSH10.Miltank_126 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=184,
    rarity=Rarities.ChrRareHolo,
    guid='05db79be-6ef2-5777-bae2-12f896760dca',
    set_code='CZ',
    key='CZ',
    regulation_mark='F',
)

card.extra_attributes["200790"] = {"type": "string", "value": "GG24"}
