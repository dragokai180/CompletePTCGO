# Gallery print swsh9tg/TG06; artwork is downloaded by the installer.
from spirit.game.scripts.cards.SWSH4.Dusknoir_71 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=192,
    rarity=Rarities.ChrRareHolo,
    guid='f4c6726d-ba42-558d-a9e0-eae085d7e6f9',
    set_code='SWSH9',
    key='SWSH9',
    regulation_mark='D',
)

card.extra_attributes["200790"] = {"type": "string", "value": "TG06"}
