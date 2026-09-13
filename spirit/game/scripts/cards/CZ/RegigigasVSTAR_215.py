# Gallery print swsh12pt5gg/GG55; artwork is downloaded by the installer.
from spirit.game.scripts.cards.CZ.RegigigasVSTAR_114 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=215,
    rarity=Rarities.RareHoloVSTAR,
    guid='3e8ee7e2-8400-53a6-9bb9-3bcf5d92c678',
    set_code='CZ',
    key='CZ',
    regulation_mark='F',
)

card.extra_attributes["200790"] = {"type": "string", "value": "GG55"}
