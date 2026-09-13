# Gallery print swsh12tg/TG06; artwork is downloaded by the installer.
from spirit.game.scripts.cards.SWSH6.Malamar_70 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=221,
    rarity=Rarities.ChrRareHolo,
    guid='9aab4b80-9169-52e0-8dbf-f7526802380b',
    set_code='SWSH12',
    key='SWSH12',
    regulation_mark='E',
)

card.extra_attributes["200790"] = {"type": "string", "value": "TG06"}
