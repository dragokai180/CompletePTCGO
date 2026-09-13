# Gallery print swsh10tg/TG07; artwork is downloaded by the installer.
from spirit.game.scripts.cards.SWSH5.Falinks_83 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=223,
    rarity=Rarities.ChrRareHolo,
    guid='d8865575-3328-549b-8052-89939c4223e6',
    set_code='SWSH10',
    key='SWSH10',
    regulation_mark='E',
)

card.extra_attributes["200790"] = {"type": "string", "value": "TG07"}
