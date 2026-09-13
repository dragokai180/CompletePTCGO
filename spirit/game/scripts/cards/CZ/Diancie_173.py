# Gallery print swsh12pt5gg/GG13; artwork is downloaded by the installer.
from spirit.game.scripts.cards.SWSH10.Diancie_68 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=173,
    rarity=Rarities.ChrRareHolo,
    guid='042ee622-d3c1-5e68-968b-36d5145293c0',
    set_code='CZ',
    key='CZ',
    regulation_mark='F',
)

card.extra_attributes["200790"] = {"type": "string", "value": "GG13"}
