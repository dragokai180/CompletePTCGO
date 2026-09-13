# Gallery print swsh9tg/TG23; artwork is downloaded by the installer.
from spirit.game.scripts.cards.SWSH7.UmbreonVMAX_95 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=209,
    rarity=Rarities.RareHoloVMAX,
    guid='a3a39c2f-5d72-52a3-9dc4-7d7e05ab490b',
    set_code='SWSH9',
    key='SWSH9',
    regulation_mark='E',
)

card.extra_attributes["200790"] = {"type": "string", "value": "TG23"}
