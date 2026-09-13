# Gallery print swsh10tg/TG13; artwork is downloaded by the installer.
from spirit.game.scripts.cards.SWSH10.StarmieV_30 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=229,
    rarity=Rarities.RareHoloV,
    guid='e9ef1ef6-f187-520d-9ceb-6ce9f6d4b646',
    set_code='SWSH10',
    key='SWSH10',
    regulation_mark='F',
)

card.extra_attributes["200790"] = {"type": "string", "value": "TG13"}
