# Gallery print swsh12pt5gg/GG50; artwork is downloaded by the installer.
from spirit.game.scripts.cards.SWSH10.DarkraiVSTAR_99 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=210,
    rarity=Rarities.RareHoloVSTAR,
    guid='12bd9548-97f3-5839-9e36-395b072d7785',
    set_code='CZ',
    key='CZ',
    regulation_mark='F',
)

card.extra_attributes["200790"] = {"type": "string", "value": "GG50"}
