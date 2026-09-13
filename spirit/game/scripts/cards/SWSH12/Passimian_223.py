# Gallery print swsh12tg/TG08; artwork is downloaded by the installer.
from spirit.game.scripts.cards.SWSH6.Passimian_88 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=223,
    rarity=Rarities.ChrRareHolo,
    guid='0c42d0aa-09b8-5284-9d5e-f9e853cf8e85',
    set_code='SWSH12',
    key='SWSH12',
    regulation_mark='E',
)

card.extra_attributes["200790"] = {"type": "string", "value": "TG08"}
