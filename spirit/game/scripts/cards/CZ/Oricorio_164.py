# Gallery print swsh12pt5gg/GG04; artwork is downloaded by the installer.
from spirit.game.scripts.cards.SWSH8.Oricorio_42 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=164,
    rarity=Rarities.ChrRareHolo,
    guid='d6bd3247-dced-5f58-8540-d46abcc6aa8e',
    set_code='CZ',
    key='CZ',
    regulation_mark='E',
)

card.extra_attributes["200790"] = {"type": "string", "value": "GG04"}
