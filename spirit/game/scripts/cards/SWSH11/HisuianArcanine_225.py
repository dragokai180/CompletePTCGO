# Gallery print swsh11tg/TG08; artwork is downloaded by the installer.
from spirit.game.scripts.cards.SWSH11.HisuianArcanine_84 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=225,
    rarity=Rarities.ChrRareHolo,
    guid='504531f7-6f49-5412-bdad-509887449d52',
    set_code='SWSH11',
    key='SWSH11',
    regulation_mark='F',
)

card.extra_attributes["200790"] = {"type": "string", "value": "TG08"}
