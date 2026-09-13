# Gallery print swsh12tg/TG03; artwork is downloaded by the installer.
from spirit.game.scripts.cards.SWSH7.Flaaffy_55 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=218,
    rarity=Rarities.ChrRareHolo,
    guid='3fa1ec4c-a1aa-5bc9-9319-0ecf9699b0ac',
    set_code='SWSH12',
    key='SWSH12',
    regulation_mark='E',
)

card.extra_attributes["200790"] = {"type": "string", "value": "TG03"}
