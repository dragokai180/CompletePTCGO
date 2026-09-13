# Gallery print swsh12pt5gg/GG42; artwork is downloaded by the installer.
from spirit.game.scripts.cards.CZ.ZeraoraVMAX_54 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=202,
    rarity=Rarities.RareHoloVMAX,
    guid='78fe694e-23c7-5321-82ca-ee1677ac365c',
    set_code='CZ',
    key='CZ',
    regulation_mark='F',
)

card.extra_attributes["200790"] = {"type": "string", "value": "GG42"}
