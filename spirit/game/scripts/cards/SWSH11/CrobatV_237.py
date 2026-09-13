# Gallery print swsh11tg/TG20; artwork is downloaded by the installer.
from spirit.game.scripts.cards.SWSH3.CrobatV_104 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=237,
    rarity=Rarities.RareHoloV,
    guid='a2db9f08-3c39-56d1-88bf-8d7b0a5ef1bd',
    set_code='SWSH11',
    key='SWSH11',
    regulation_mark='D',
)

card.extra_attributes["200790"] = {"type": "string", "value": "TG20"}
