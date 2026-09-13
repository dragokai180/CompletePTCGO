# Gallery print swsh12tg/TG20; artwork is downloaded by the installer.
from spirit.game.scripts.cards.SWSH7.RayquazaVMAX_111 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=235,
    rarity=Rarities.RareHoloVMAX,
    guid='ec5a6dc1-3dc0-5f08-9095-7b3e12a62633',
    set_code='SWSH12',
    key='SWSH12',
    regulation_mark='E',
)

card.extra_attributes["200790"] = {"type": "string", "value": "TG20"}
