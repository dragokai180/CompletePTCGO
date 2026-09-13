# Gallery print swsh9tg/TG14; artwork is downloaded by the installer.
from spirit.game.scripts.cards.SWSH7.SylveonV_74 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=200,
    rarity=Rarities.RareHoloV,
    guid='5b5a955d-6272-50df-b08c-e514246c0378',
    set_code='SWSH9',
    key='SWSH9',
    regulation_mark='E',
)

card.extra_attributes["200790"] = {"type": "string", "value": "TG14"}
