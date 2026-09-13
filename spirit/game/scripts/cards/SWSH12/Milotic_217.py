# Gallery print swsh12tg/TG02; artwork is downloaded by the installer.
from spirit.game.scripts.cards.SWSH12.Milotic_40 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=217,
    rarity=Rarities.ChrRareHolo,
    guid='0c2f1086-ea28-5523-8b32-a8908206c827',
    set_code='SWSH12',
    key='SWSH12',
    regulation_mark='F',
)

card.extra_attributes["200790"] = {"type": "string", "value": "TG02"}
