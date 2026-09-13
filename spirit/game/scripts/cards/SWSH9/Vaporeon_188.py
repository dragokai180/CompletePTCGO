# Gallery print swsh9tg/TG02; artwork is downloaded by the installer.
from spirit.game.scripts.cards.SWSH4.Vaporeon_30 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=188,
    rarity=Rarities.ChrRareHolo,
    guid='cabf8d14-3e00-555c-99dc-425f7c333f95',
    set_code='SWSH9',
    key='SWSH9',
    regulation_mark='D',
)

card.extra_attributes["200790"] = {"type": "string", "value": "TG02"}
