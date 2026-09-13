# Gallery print swsh10tg/TG19; artwork is downloaded by the installer.
from spirit.game.scripts.cards.SWSH6.GalarianZapdosV_80 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=235,
    rarity=Rarities.RareHoloV,
    guid='dedfea84-dfe0-57e3-8473-7464b89571f5',
    set_code='SWSH10',
    key='SWSH10',
    regulation_mark='E',
)

card.extra_attributes["200790"] = {"type": "string", "value": "TG19"}
