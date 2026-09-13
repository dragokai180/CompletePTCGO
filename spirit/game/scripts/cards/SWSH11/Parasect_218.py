# Gallery print swsh11tg/TG01; artwork is downloaded by the installer.
from spirit.game.scripts.cards.SWSH11.Parasect_5 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=218,
    rarity=Rarities.ChrRareHolo,
    guid='11f3ce64-4546-5e20-8e69-e7c6468a83c7',
    set_code='SWSH11',
    key='SWSH11',
    regulation_mark='F',
)

card.extra_attributes["200790"] = {"type": "string", "value": "TG01"}
