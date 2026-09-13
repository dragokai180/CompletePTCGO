# Gallery print swsh12pt5gg/GG10; artwork is downloaded by the installer.
from spirit.game.scripts.cards.CEL25.Mew_11 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=170,
    rarity=Rarities.ChrRareHolo,
    guid='a70579f4-bdec-5b42-84da-e7f4fba64aa9',
    set_code='CZ',
    key='CZ',
    regulation_mark='E',
)

card.extra_attributes["200790"] = {"type": "string", "value": "GG10"}
