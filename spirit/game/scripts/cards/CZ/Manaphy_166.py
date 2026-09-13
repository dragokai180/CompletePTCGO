# Gallery print swsh12pt5gg/GG06; artwork is downloaded by the installer.
from spirit.game.scripts.cards.SWSH9.Manaphy_41 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=166,
    rarity=Rarities.ChrRareHolo,
    guid='34ec0c72-e492-5d78-a3cd-f7ab5cb10041',
    set_code='CZ',
    key='CZ',
    regulation_mark='F',
)

card.extra_attributes["200790"] = {"type": "string", "value": "GG06"}
