# Gallery print swsh11tg/TG21; artwork is downloaded by the installer.
from spirit.game.scripts.cards.SWSH3.EternatusV_116 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=238,
    rarity=Rarities.RareHoloV,
    guid='70e51471-a6e2-5468-86d7-54230e6a81e4',
    set_code='SWSH11',
    key='SWSH11',
    regulation_mark='D',
)

card.extra_attributes["200790"] = {"type": "string", "value": "TG21"}
