# Gallery print swsh11tg/TG09; artwork is downloaded by the installer.
from spirit.game.scripts.cards.SWSH11.Spiritomb_117 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=226,
    rarity=Rarities.ChrRareHolo,
    guid='5cf7d308-79ab-5bca-a516-d51a1a5f3425',
    set_code='SWSH11',
    key='SWSH11',
    regulation_mark='F',
)

card.extra_attributes["200790"] = {"type": "string", "value": "TG09"}
