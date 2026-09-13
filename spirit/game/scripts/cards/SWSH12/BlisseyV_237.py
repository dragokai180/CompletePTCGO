# Gallery print swsh12tg/TG22; artwork is downloaded by the installer.
from spirit.game.scripts.cards.SWSH6.BlisseyV_119 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=237,
    rarity=Rarities.RareHoloV,
    guid='b2ac8c83-d830-5d79-88df-864e49c40c9e',
    set_code='SWSH12',
    key='SWSH12',
    regulation_mark='E',
)

card.extra_attributes["200790"] = {"type": "string", "value": "TG22"}
