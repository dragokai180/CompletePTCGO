# Gallery print swsh12pt5gg/GG70; artwork is downloaded by the installer.
from spirit.game.scripts.cards.SWSH9.ArceusVSTAR_123 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=230,
    rarity=Rarities.RareSecret,
    guid='b8e247b4-0cc9-585e-b642-d2daeb0291a6',
    set_code='CZ',
    key='CZ',
    regulation_mark='F',
)

card.extra_attributes["200790"] = {"type": "string", "value": "GG70"}
