# Gallery print swsh12tg/TG07; artwork is downloaded by the installer.
from spirit.game.scripts.cards.SWSH6.Rockruff_86 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=222,
    rarity=Rarities.ChrRareHolo,
    guid='2a4775d5-6eee-5a87-938c-b17804e5a446',
    set_code='SWSH12',
    key='SWSH12',
    regulation_mark='E',
)

card.extra_attributes["200790"] = {"type": "string", "value": "TG07"}
