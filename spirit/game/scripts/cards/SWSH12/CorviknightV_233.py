# Gallery print swsh12tg/TG18; artwork is downloaded by the installer.
from spirit.game.scripts.cards.SWSH5.CorviknightV_109 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=233,
    rarity=Rarities.RareHoloV,
    guid='8a9083b2-4dc6-5495-80f1-6fecde736c4f',
    set_code='SWSH12',
    key='SWSH12',
    regulation_mark='E',
)

card.extra_attributes["200790"] = {"type": "string", "value": "TG18"}
