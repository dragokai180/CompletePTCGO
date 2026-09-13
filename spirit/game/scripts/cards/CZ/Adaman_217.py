# Gallery print swsh12pt5gg/GG57; artwork is downloaded by the installer.
from spirit.game.scripts.cards.SWSH10.Adaman_135 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=217,
    rarity=Rarities.RareUltra,
    guid='7a52ffea-6d2e-5027-9354-cf708b0a96cb',
    set_code='CZ',
    key='CZ',
    regulation_mark='F',
)

card.extra_attributes["200790"] = {"type": "string", "value": "GG57"}
