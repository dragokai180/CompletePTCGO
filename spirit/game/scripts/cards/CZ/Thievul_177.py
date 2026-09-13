# Gallery print swsh12pt5gg/GG17; artwork is downloaded by the installer.
from spirit.game.scripts.cards.SWSH10.Thievul_104 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=177,
    rarity=Rarities.ChrRareHolo,
    guid='2080bee0-5528-589b-bd54-71b60d9f7021',
    set_code='CZ',
    key='CZ',
    regulation_mark='F',
)

card.extra_attributes["200790"] = {"type": "string", "value": "GG17"}
