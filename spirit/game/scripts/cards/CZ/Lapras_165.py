# Gallery print swsh12pt5gg/GG05; artwork is downloaded by the installer.
from spirit.game.scripts.cards.SWSH9.Lapras_31 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=165,
    rarity=Rarities.ChrRareHolo,
    guid='7bd93e35-b412-5541-b029-32367b26865e',
    set_code='CZ',
    key='CZ',
    regulation_mark='F',
)

card.extra_attributes["200790"] = {"type": "string", "value": "GG05"}
