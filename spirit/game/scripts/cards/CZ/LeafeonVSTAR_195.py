# Gallery print swsh12pt5gg/GG35; artwork is downloaded by the installer.
from spirit.game.scripts.cards.CZ.LeafeonVSTAR_14 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=195,
    rarity=Rarities.RareHoloVSTAR,
    guid='3b52d26b-baa4-5a58-9e3a-13e84cb6f26a',
    set_code='CZ',
    key='CZ',
    regulation_mark='F',
)

card.extra_attributes["200790"] = {"type": "string", "value": "GG35"}
