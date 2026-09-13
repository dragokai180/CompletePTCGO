# Gallery print swsh11tg/TG02; artwork is downloaded by the installer.
from spirit.game.scripts.cards.SWSH11.Roserade_15 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=219,
    rarity=Rarities.ChrRareHolo,
    guid='32a1c391-b535-5fec-ad4a-4dbf4651683a',
    set_code='SWSH11',
    key='SWSH11',
    regulation_mark='F',
)

card.extra_attributes["200790"] = {"type": "string", "value": "TG02"}
