# Gallery print swsh12pt5gg/GG44; artwork is downloaded by the installer.
from spirit.game.scripts.cards.PGO.MewtwoVSTAR_31 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=204,
    rarity=Rarities.RareHoloVSTAR,
    guid='30b8dc56-bcf5-5bac-9c00-28a90572b407',
    set_code='CZ',
    key='CZ',
    regulation_mark='F',
)

card.extra_attributes["200790"] = {"type": "string", "value": "GG44"}
