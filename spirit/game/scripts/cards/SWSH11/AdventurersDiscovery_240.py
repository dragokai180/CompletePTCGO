# Gallery print swsh11tg/TG23; artwork is downloaded by the installer.
from spirit.game.scripts.cards.SWSH8.AdventurersDiscovery_224 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=240,
    rarity=Rarities.RareUltra,
    guid='90fa94f6-0135-5487-83a4-42ea9391db0c',
    set_code='SWSH11',
    key='SWSH11',
    regulation_mark='E',
)

card.extra_attributes["200790"] = {"type": "string", "value": "TG23"}
