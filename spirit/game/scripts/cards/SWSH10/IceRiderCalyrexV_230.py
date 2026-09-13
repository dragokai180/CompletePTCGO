# Gallery print swsh10tg/TG14; artwork is downloaded by the installer.
from spirit.game.scripts.cards.SWSH6.IceRiderCalyrexV_45 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=230,
    rarity=Rarities.RareHoloV,
    guid='95271e08-2bcc-522a-853a-3c918b94c12f',
    set_code='SWSH10',
    key='SWSH10',
    regulation_mark='E',
)

card.extra_attributes["200790"] = {"type": "string", "value": "TG14"}
