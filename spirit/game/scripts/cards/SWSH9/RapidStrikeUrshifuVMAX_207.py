# Gallery print swsh9tg/TG21; artwork is downloaded by the installer.
from spirit.game.scripts.cards.SWSH5.RapidStrikeUrshifuVMAX_88 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=207,
    rarity=Rarities.RareHoloVMAX,
    guid='9e76f102-c402-50c6-9c4a-ea6593c36ae6',
    set_code='SWSH9',
    key='SWSH9',
    regulation_mark='E',
)

card.extra_attributes["200790"] = {"type": "string", "value": "TG21"}
