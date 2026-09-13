# Gallery print swsh9tg/TG28; artwork is downloaded by the installer.
from spirit.game.scripts.cards.SWSH5.SingleStrikeStyleMustard_134 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=214,
    rarity=Rarities.RareUltra,
    guid='abacbd25-f0a4-51ac-ba0c-40fbd97e52cc',
    set_code='SWSH9',
    key='SWSH9',
    regulation_mark='E',
)

card.extra_attributes["200790"] = {"type": "string", "value": "TG28"}
