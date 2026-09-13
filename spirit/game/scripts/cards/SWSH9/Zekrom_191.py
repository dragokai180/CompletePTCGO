# Gallery print swsh9tg/TG05; artwork is downloaded by the installer.
from spirit.game.scripts.cards.SWSH4.Zekrom_60 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=191,
    rarity=Rarities.ChrRareHolo,
    guid='950ffd37-7268-52c6-bd50-68e3f4661076',
    set_code='SWSH9',
    key='SWSH9',
    regulation_mark='D',
)

card.extra_attributes["200790"] = {"type": "string", "value": "TG05"}
