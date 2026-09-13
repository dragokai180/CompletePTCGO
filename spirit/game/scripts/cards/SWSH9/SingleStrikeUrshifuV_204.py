# Gallery print swsh9tg/TG18; artwork is downloaded by the installer.
from spirit.game.scripts.cards.SWSH5.SingleStrikeUrshifuV_85 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=204,
    rarity=Rarities.RareHoloV,
    guid='50b11dfa-5347-578e-930e-c127b9efed27',
    set_code='SWSH9',
    key='SWSH9',
    regulation_mark='E',
)

card.extra_attributes["200790"] = {"type": "string", "value": "TG18"}
