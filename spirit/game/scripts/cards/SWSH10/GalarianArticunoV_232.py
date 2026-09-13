# Gallery print swsh10tg/TG16; artwork is downloaded by the installer.
from spirit.game.scripts.cards.SWSH6.GalarianArticunoV_58 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=232,
    rarity=Rarities.RareHoloV,
    guid='7b7f240c-0e63-5a5d-964d-0b456ab3ef77',
    set_code='SWSH10',
    key='SWSH10',
    regulation_mark='E',
)

card.extra_attributes["200790"] = {"type": "string", "value": "TG16"}
