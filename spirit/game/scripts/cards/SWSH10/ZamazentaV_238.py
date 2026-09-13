# Gallery print swsh10tg/TG22; artwork is downloaded by the installer.
from spirit.game.scripts.cards.SWSH1.ZamazentaV_139 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=238,
    rarity=Rarities.RareHoloV,
    guid='760aba2c-f9ac-59cc-ad33-03e86e4e4d78',
    set_code='SWSH10',
    key='SWSH10',
    regulation_mark='D',
)

card.extra_attributes["200790"] = {"type": "string", "value": "TG22"}
