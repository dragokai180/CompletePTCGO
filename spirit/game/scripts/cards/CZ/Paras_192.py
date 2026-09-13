# Gallery print swsh12pt5gg/GG32; artwork is downloaded by the installer.
from spirit.game.scripts.cards.SWSH11.Paras_4 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=192,
    rarity=Rarities.ChrRareHolo,
    guid='fed4b84a-5135-507e-a9f9-307a5f6a46c1',
    set_code='CZ',
    key='CZ',
    regulation_mark='F',
)

card.extra_attributes["200790"] = {"type": "string", "value": "GG32"}
