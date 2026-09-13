# Gallery print swsh12pt5gg/GG14; artwork is downloaded by the installer.
from spirit.game.scripts.cards.SWSH11.Comfey_79 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=174,
    rarity=Rarities.ChrRareHolo,
    guid='5446d60d-7c36-5b9b-8ee8-412b7a97315a',
    set_code='CZ',
    key='CZ',
    regulation_mark='F',
)

card.extra_attributes["200790"] = {"type": "string", "value": "GG14"}
