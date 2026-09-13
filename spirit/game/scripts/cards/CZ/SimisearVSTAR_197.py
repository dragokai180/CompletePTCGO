# Gallery print swsh12pt5gg/GG37; artwork is downloaded by the installer.
from spirit.game.scripts.cards.CZ.SimisearVSTAR_23 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=197,
    rarity=Rarities.RareHoloVSTAR,
    guid='a0ec8818-56ea-53b2-8c96-283d39cb0bd2',
    set_code='CZ',
    key='CZ',
    regulation_mark='F',
)

card.extra_attributes["200790"] = {"type": "string", "value": "GG37"}
