# Gallery print swsh12pt5gg/GG54; artwork is downloaded by the installer.
from spirit.game.scripts.cards.SWSH9.ZamazentaV_105 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=214,
    rarity=Rarities.RareHoloV,
    guid='7e8e2e36-d2fd-5655-bb26-46afc9626172',
    set_code='CZ',
    key='CZ',
    regulation_mark='F',
)

card.extra_attributes["200790"] = {"type": "string", "value": "GG54"}
