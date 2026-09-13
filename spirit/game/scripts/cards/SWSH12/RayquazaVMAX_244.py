# Gallery print swsh12tg/TG29; artwork is downloaded by the installer.
from spirit.game.scripts.cards.SWSH7.RayquazaVMAX_111 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=244,
    rarity=Rarities.RareSecret,
    guid='eb7396f0-e455-5ceb-b3ad-252652894ff0',
    set_code='SWSH12',
    key='SWSH12',
    regulation_mark='E',
)

card.extra_attributes["200790"] = {"type": "string", "value": "TG29"}
