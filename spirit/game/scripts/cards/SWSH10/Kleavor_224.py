# Gallery print swsh10tg/TG08; artwork is downloaded by the installer.
from spirit.game.scripts.cards.SWSH10.Kleavor_86 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=224,
    rarity=Rarities.ChrRareHolo,
    guid='b1febf35-587d-5802-b0cf-ac11ef87a791',
    set_code='SWSH10',
    key='SWSH10',
    regulation_mark='F',
)

card.extra_attributes["200790"] = {"type": "string", "value": "TG08"}
