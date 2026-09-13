# Gallery print swsh12pt5gg/GG01; artwork is downloaded by the installer.
from spirit.game.scripts.cards.SWSH10.HisuianVoltorb_2 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=161,
    rarity=Rarities.ChrRareHolo,
    guid='23435d80-9c51-531f-86bf-2af730e5f8ed',
    set_code='CZ',
    key='CZ',
    regulation_mark='F',
)

card.extra_attributes["200790"] = {"type": "string", "value": "GG01"}
