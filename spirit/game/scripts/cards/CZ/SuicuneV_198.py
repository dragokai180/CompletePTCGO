# Gallery print swsh12pt5gg/GG38; artwork is downloaded by the installer.
from spirit.game.scripts.cards.SWSH7.SuicuneV_31 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=198,
    rarity=Rarities.RareHoloV,
    guid='cb177572-6fc7-52ea-9434-0a6ffbd58e85',
    set_code='CZ',
    key='CZ',
    regulation_mark='E',
)

card.extra_attributes["200790"] = {"type": "string", "value": "GG38"}
