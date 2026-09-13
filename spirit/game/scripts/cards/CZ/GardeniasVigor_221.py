# Gallery print swsh12pt5gg/GG61; artwork is downloaded by the installer.
from spirit.game.scripts.cards.SWSH10.GardeniasVigor_143 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=221,
    rarity=Rarities.RareUltra,
    guid='583f77bf-13c2-5252-a6fa-4ec073e62c09',
    set_code='CZ',
    key='CZ',
    regulation_mark='F',
)

card.extra_attributes["200790"] = {"type": "string", "value": "GG61"}
