# Gallery print swsh12pt5gg/GG19; artwork is downloaded by the installer.
from spirit.game.scripts.cards.SWSH7.Altaria_106 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=179,
    rarity=Rarities.ChrRareHolo,
    guid='d98cdea9-f730-5637-98c9-fc71a38d4495',
    set_code='CZ',
    key='CZ',
    regulation_mark='E',
)

card.extra_attributes["200790"] = {"type": "string", "value": "GG19"}
