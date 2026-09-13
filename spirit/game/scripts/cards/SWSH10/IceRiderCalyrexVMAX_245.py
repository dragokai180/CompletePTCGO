# Gallery print swsh10tg/TG29; artwork is downloaded by the installer.
from spirit.game.scripts.cards.SWSH6.IceRiderCalyrexVMAX_46 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=245,
    rarity=Rarities.RareSecret,
    guid='d61b1a9b-53fa-5837-a800-5178bccdbd62',
    set_code='SWSH10',
    key='SWSH10',
    regulation_mark='E',
)

card.extra_attributes["200790"] = {"type": "string", "value": "TG29"}
