# Gallery print swsh12tg/TG12; artwork is downloaded by the installer.
from spirit.game.scripts.cards.SWSH5.KricketuneV_6 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=227,
    rarity=Rarities.RareHoloV,
    guid='e8a8a506-3550-53f4-a14b-806f51831b98',
    set_code='SWSH12',
    key='SWSH12',
    regulation_mark='E',
)

card.extra_attributes["200790"] = {"type": "string", "value": "TG12"}
