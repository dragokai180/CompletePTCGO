# Gallery print swsh10tg/TG20; artwork is downloaded by the installer.
from spirit.game.scripts.cards.SWSH6.GalarianMoltresV_97 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=236,
    rarity=Rarities.RareHoloV,
    guid='d2211966-1907-591e-97cd-4a08c7af21ee',
    set_code='SWSH10',
    key='SWSH10',
    regulation_mark='E',
)

card.extra_attributes["200790"] = {"type": "string", "value": "TG20"}
