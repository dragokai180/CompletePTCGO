# Gallery print swsh12pt5gg/GG33; artwork is downloaded by the installer.
from spirit.game.scripts.cards.SWSH10.Poochyena_95 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=193,
    rarity=Rarities.ChrRareHolo,
    guid='f25b29fa-ae9a-5458-af7c-9c4d2d03f4a1',
    set_code='CZ',
    key='CZ',
    regulation_mark='F',
)

card.extra_attributes["200790"] = {"type": "string", "value": "GG33"}
