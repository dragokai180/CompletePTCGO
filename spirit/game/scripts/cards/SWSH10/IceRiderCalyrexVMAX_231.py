# Gallery print swsh10tg/TG15; artwork is downloaded by the installer.
from spirit.game.scripts.cards.SWSH6.IceRiderCalyrexVMAX_46 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=231,
    rarity=Rarities.RareHoloVMAX,
    guid='939acca4-2383-5459-9386-f66eb6c6963b',
    set_code='SWSH10',
    key='SWSH10',
    regulation_mark='E',
)

card.extra_attributes["200790"] = {"type": "string", "value": "TG15"}
