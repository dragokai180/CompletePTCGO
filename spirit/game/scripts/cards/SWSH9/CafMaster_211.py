# Gallery print swsh9tg/TG25; artwork is downloaded by the installer.
from spirit.game.scripts.cards.SWSH9.CafMaster_133 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=211,
    rarity=Rarities.RareUltra,
    guid='0a0bca50-218c-5050-863b-b8feb6b825b2',
    set_code='SWSH9',
    key='SWSH9',
    regulation_mark='E',
)

card.extra_attributes["200790"] = {"type": "string", "value": "TG25"}
