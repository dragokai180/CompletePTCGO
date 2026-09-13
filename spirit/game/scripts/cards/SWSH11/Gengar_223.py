# Gallery print swsh11tg/TG06; artwork is downloaded by the installer.
from spirit.game.scripts.cards.SWSH11.Gengar_66 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=223,
    rarity=Rarities.ChrRareHolo,
    guid='4376f0d2-1964-584e-9dcb-831ff2287ccf',
    set_code='SWSH11',
    key='SWSH11',
    regulation_mark='F',
)

card.extra_attributes["200790"] = {"type": "string", "value": "TG06"}
