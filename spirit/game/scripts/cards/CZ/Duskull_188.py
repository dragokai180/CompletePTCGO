# Gallery print swsh12pt5gg/GG28; artwork is downloaded by the installer.
from spirit.game.scripts.cards.SWSH9.Duskull_60 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=188,
    rarity=Rarities.ChrRareHolo,
    guid='d368114e-64b2-5edf-802d-e086be56da01',
    set_code='CZ',
    key='CZ',
    regulation_mark='F',
)

card.extra_attributes["200790"] = {"type": "string", "value": "GG28"}
