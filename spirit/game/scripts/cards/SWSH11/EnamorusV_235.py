# Gallery print swsh11tg/TG18; artwork is downloaded by the installer.
from spirit.game.scripts.cards.SWSH11.EnamorusV_82 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=235,
    rarity=Rarities.RareHoloV,
    guid='b2fbebe7-48c7-534d-9701-7e2fec8dfa86',
    set_code='SWSH11',
    key='SWSH11',
    regulation_mark='F',
)

card.extra_attributes["200790"] = {"type": "string", "value": "TG18"}
