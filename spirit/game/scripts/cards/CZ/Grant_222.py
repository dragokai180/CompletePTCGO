# Gallery print swsh12pt5gg/GG62; artwork is downloaded by the installer.
from spirit.game.scripts.cards.SWSH10.Grant_144 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=222,
    rarity=Rarities.RareUltra,
    guid='f5d53c4a-d343-541d-a367-7ad05760d737',
    set_code='CZ',
    key='CZ',
    regulation_mark='F',
)

card.extra_attributes["200790"] = {"type": "string", "value": "GG62"}
