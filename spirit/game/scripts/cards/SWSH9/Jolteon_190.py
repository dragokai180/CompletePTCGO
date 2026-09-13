# Gallery print swsh9tg/TG04; artwork is downloaded by the installer.
from spirit.game.scripts.cards.SWSH4.Jolteon_47 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=190,
    rarity=Rarities.ChrRareHolo,
    guid='f7dadd6b-3d06-5c3b-8873-577b7e9c8149',
    set_code='SWSH9',
    key='SWSH9',
    regulation_mark='D',
)

card.extra_attributes["200790"] = {"type": "string", "value": "TG04"}
