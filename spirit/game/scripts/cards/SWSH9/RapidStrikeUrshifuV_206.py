# Gallery print swsh9tg/TG20; artwork is downloaded by the installer.
from spirit.game.scripts.cards.SWSH5.RapidStrikeUrshifuV_87 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=206,
    rarity=Rarities.RareHoloV,
    guid='72bc314e-a050-5460-ab32-6517411fe25d',
    set_code='SWSH9',
    key='SWSH9',
    regulation_mark='E',
)

card.extra_attributes["200790"] = {"type": "string", "value": "TG20"}
