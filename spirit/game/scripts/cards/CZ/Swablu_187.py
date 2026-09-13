# Gallery print swsh12pt5gg/GG27; artwork is downloaded by the installer.
from spirit.game.scripts.cards.SWSH7.Swablu_132 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=187,
    rarity=Rarities.ChrRareHolo,
    guid='9d3cad2b-fbc3-5235-b9bc-f70f44709555',
    set_code='CZ',
    key='CZ',
    regulation_mark='E',
)

card.extra_attributes["200790"] = {"type": "string", "value": "GG27"}
