# Gallery print swsh9tg/TG11; artwork is downloaded by the installer.
from spirit.game.scripts.cards.SWSH7.Eevee_125 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=197,
    rarity=Rarities.ChrRareHolo,
    guid='8a904e8e-9d2e-543e-8351-f2bf23d7e448',
    set_code='SWSH9',
    key='SWSH9',
    regulation_mark='E',
)

card.extra_attributes["200790"] = {"type": "string", "value": "TG11"}
