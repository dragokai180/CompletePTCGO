# Gallery print swsh12pt5gg/GG58; artwork is downloaded by the installer.
from spirit.game.scripts.cards.SWSH9.CherensCare_134 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=218,
    rarity=Rarities.RareUltra,
    guid='be3a4af4-09f0-5265-a30a-ffae7cd4e978',
    set_code='CZ',
    key='CZ',
    regulation_mark='F',
)

card.extra_attributes["200790"] = {"type": "string", "value": "GG58"}
