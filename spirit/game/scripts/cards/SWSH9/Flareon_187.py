# Gallery print swsh9tg/TG01; artwork is downloaded by the installer.
from spirit.game.scripts.cards.SWSH4.Flareon_26 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=187,
    rarity=Rarities.ChrRareHolo,
    guid='ca031865-c59c-5bde-ac4d-2abbe3f65b85',
    set_code='SWSH9',
    key='SWSH9',
    regulation_mark='D',
)

card.extra_attributes["200790"] = {"type": "string", "value": "TG01"}
