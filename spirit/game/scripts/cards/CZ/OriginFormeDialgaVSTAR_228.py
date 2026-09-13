# Gallery print swsh12pt5gg/GG68; artwork is downloaded by the installer.
from spirit.game.scripts.cards.SWSH10.OriginFormeDialgaVSTAR_114 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=228,
    rarity=Rarities.RareSecret,
    guid='9bc76c5c-76d4-5fde-a27a-6e007d034857',
    set_code='CZ',
    key='CZ',
    regulation_mark='F',
)

card.extra_attributes["200790"] = {"type": "string", "value": "GG68"}
