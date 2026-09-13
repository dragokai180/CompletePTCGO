# Gallery print swsh10tg/TG23; artwork is downloaded by the installer.
from spirit.game.scripts.cards.SWSH10.GarchompV_117 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=239,
    rarity=Rarities.RareHoloV,
    guid='4c368823-d862-51eb-addf-bedb73b4d18b',
    set_code='SWSH10',
    key='SWSH10',
    regulation_mark='F',
)

card.extra_attributes["200790"] = {"type": "string", "value": "TG23"}
