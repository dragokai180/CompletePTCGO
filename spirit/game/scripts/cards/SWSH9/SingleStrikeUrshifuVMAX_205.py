# Gallery print swsh9tg/TG19; artwork is downloaded by the installer.
from spirit.game.scripts.cards.SWSH5.SingleStrikeUrshifuVMAX_86 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=205,
    rarity=Rarities.RareHoloVMAX,
    guid='c16f9aba-aa90-5ad0-bbcb-3daf8e33be97',
    set_code='SWSH9',
    key='SWSH9',
    regulation_mark='E',
)

card.extra_attributes["200790"] = {"type": "string", "value": "TG19"}
