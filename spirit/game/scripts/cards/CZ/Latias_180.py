# Gallery print swsh12pt5gg/GG20; artwork is downloaded by the installer.
from spirit.game.scripts.cards.SWSH8.Latias_193 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=180,
    rarity=Rarities.ChrRareHolo,
    guid='4292127a-f02c-5268-837b-8813853d04b2',
    set_code='CZ',
    key='CZ',
    regulation_mark='E',
)

card.extra_attributes["200790"] = {"type": "string", "value": "GG20"}
