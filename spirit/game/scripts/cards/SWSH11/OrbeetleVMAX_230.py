# Gallery print swsh11tg/TG13; artwork is downloaded by the installer.
from spirit.game.scripts.cards.SWSH4.OrbeetleVMAX_21 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=230,
    rarity=Rarities.RareHoloVMAX,
    guid='beb561db-b431-586b-a3f2-656dc9dea5d4',
    set_code='SWSH11',
    key='SWSH11',
    regulation_mark='D',
)

card.extra_attributes["200790"] = {"type": "string", "value": "TG13"}
