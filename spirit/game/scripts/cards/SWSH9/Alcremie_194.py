# Gallery print swsh9tg/TG08; artwork is downloaded by the installer.
from spirit.game.scripts.cards.SWSH9.Alcremie_71 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=194,
    rarity=Rarities.ChrRareHolo,
    guid='dcb84769-68c8-5212-9964-36487742bf27',
    set_code='SWSH9',
    key='SWSH9',
    regulation_mark='E',
)

card.extra_attributes["200790"] = {"type": "string", "value": "TG08"}
