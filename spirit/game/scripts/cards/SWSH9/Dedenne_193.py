# Gallery print swsh9tg/TG07; artwork is downloaded by the installer.
from spirit.game.scripts.cards.SWSH9.Dedenne_67 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=193,
    rarity=Rarities.ChrRareHolo,
    guid='dc2babe9-1399-534b-b052-92f732835639',
    set_code='SWSH9',
    key='SWSH9',
    regulation_mark='E',
)

card.extra_attributes["200790"] = {"type": "string", "value": "TG07"}
