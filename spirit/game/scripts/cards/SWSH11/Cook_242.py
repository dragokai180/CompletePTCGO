# Gallery print swsh11tg/TG25; artwork is downloaded by the installer.
from spirit.game.scripts.cards.SWSH8.Cook_228 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=242,
    rarity=Rarities.RareUltra,
    guid='8a5e021e-5419-5ccd-a135-511b86cc1597',
    set_code='SWSH11',
    key='SWSH11',
    regulation_mark='E',
)

card.extra_attributes["200790"] = {"type": "string", "value": "TG25"}
