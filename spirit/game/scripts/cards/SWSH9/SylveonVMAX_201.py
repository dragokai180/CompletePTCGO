# Gallery print swsh9tg/TG15; artwork is downloaded by the installer.
from spirit.game.scripts.cards.SWSH7.SylveonVMAX_75 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=201,
    rarity=Rarities.RareHoloVMAX,
    guid='4c30257b-7259-5240-b744-0f55ca8794eb',
    set_code='SWSH9',
    key='SWSH9',
    regulation_mark='E',
)

card.extra_attributes["200790"] = {"type": "string", "value": "TG15"}
