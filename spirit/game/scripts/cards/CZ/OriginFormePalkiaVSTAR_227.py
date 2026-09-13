# Gallery print swsh12pt5gg/GG67; artwork is downloaded by the installer.
from spirit.game.scripts.cards.SWSH10.OriginFormePalkiaVSTAR_40 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=227,
    rarity=Rarities.RareSecret,
    guid='41cfd6d0-8aa8-5c7f-9ed0-a9a3f899d010',
    set_code='CZ',
    key='CZ',
    regulation_mark='F',
)

card.extra_attributes["200790"] = {"type": "string", "value": "GG67"}
