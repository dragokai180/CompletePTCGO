# Gallery print swsh11tg/TG12; artwork is downloaded by the installer.
from spirit.game.scripts.cards.SWSH4.OrbeetleV_20 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=229,
    rarity=Rarities.RareHoloV,
    guid='a52fef3a-3ff7-5829-9f46-2269f4eb7e19',
    set_code='SWSH11',
    key='SWSH11',
    regulation_mark='D',
)

card.extra_attributes["200790"] = {"type": "string", "value": "TG12"}
