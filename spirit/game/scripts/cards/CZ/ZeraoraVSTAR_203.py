# Gallery print swsh12pt5gg/GG43; artwork is downloaded by the installer.
from spirit.game.scripts.cards.CZ.ZeraoraVSTAR_55 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=203,
    rarity=Rarities.RareHoloVSTAR,
    guid='f1973b68-9d1f-5022-a827-605f24cbc06e',
    set_code='CZ',
    key='CZ',
    regulation_mark='F',
)

card.extra_attributes["200790"] = {"type": "string", "value": "GG43"}
