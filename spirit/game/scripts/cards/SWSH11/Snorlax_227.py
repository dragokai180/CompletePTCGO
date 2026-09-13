# Gallery print swsh11tg/TG10; artwork is downloaded by the installer.
from spirit.game.scripts.cards.SWSH11.Snorlax_143 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=227,
    rarity=Rarities.ChrRareHolo,
    guid='62e43f8e-4d98-5c88-8c32-48cb1f925086',
    set_code='SWSH11',
    key='SWSH11',
    regulation_mark='F',
)

card.extra_attributes["200790"] = {"type": "string", "value": "TG10"}
