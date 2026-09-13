# Gallery print swsh11tg/TG22; artwork is downloaded by the installer.
from spirit.game.scripts.cards.SWSH3.EternatusVMAX_117 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=239,
    rarity=Rarities.RareHoloVMAX,
    guid='c9f34e4f-7854-5b94-a2bc-a18d48795b13',
    set_code='SWSH11',
    key='SWSH11',
    regulation_mark='D',
)

card.extra_attributes["200790"] = {"type": "string", "value": "TG22"}
