# Gallery print swsh12pt5gg/GG41; artwork is downloaded by the installer.
from spirit.game.scripts.cards.SWSH9.RaikouV_48 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=201,
    rarity=Rarities.RareHoloV,
    guid='00e360bb-926f-597c-bc39-eb8bd504cdba',
    set_code='CZ',
    key='CZ',
    regulation_mark='F',
)

card.extra_attributes["200790"] = {"type": "string", "value": "GG41"}
