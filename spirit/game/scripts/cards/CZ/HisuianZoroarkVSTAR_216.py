# Gallery print swsh12pt5gg/GG56; artwork is downloaded by the installer.
from spirit.game.scripts.cards.SWSH11.HisuianZoroarkVSTAR_147 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=216,
    rarity=Rarities.RareHoloVSTAR,
    guid='bc0b914d-b29c-508f-9a20-9c928a9761fa',
    set_code='CZ',
    key='CZ',
    regulation_mark='F',
)

card.extra_attributes["200790"] = {"type": "string", "value": "GG56"}
