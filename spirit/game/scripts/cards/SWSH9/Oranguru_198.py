# Gallery print swsh9tg/TG12; artwork is downloaded by the installer.
from spirit.game.scripts.cards.SWSH1.Oranguru_148 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=198,
    rarity=Rarities.ChrRareHolo,
    guid='2b191c7b-b3e9-5125-811f-a95057813806',
    set_code='SWSH9',
    key='SWSH9',
    regulation_mark='D',
)

card.extra_attributes["200790"] = {"type": "string", "value": "TG12"}
