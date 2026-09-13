# Gallery print swsh12pt5gg/GG21; artwork is downloaded by the installer.
from spirit.game.scripts.cards.SWSH11.HisuianGoodra_134 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=181,
    rarity=Rarities.ChrRareHolo,
    guid='bea04285-4d3f-56f1-8db9-7a002344c168',
    set_code='CZ',
    key='CZ',
    regulation_mark='F',
)

card.extra_attributes["200790"] = {"type": "string", "value": "GG21"}
