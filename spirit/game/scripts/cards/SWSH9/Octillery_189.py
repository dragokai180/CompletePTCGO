# Gallery print swsh9tg/TG03; artwork is downloaded by the installer.
from spirit.game.scripts.cards.SWSH5.Octillery_37 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=189,
    rarity=Rarities.ChrRareHolo,
    guid='47d68d32-476c-513c-932c-bc109eee3173',
    set_code='SWSH9',
    key='SWSH9',
    regulation_mark='E',
)

card.extra_attributes["200790"] = {"type": "string", "value": "TG03"}
