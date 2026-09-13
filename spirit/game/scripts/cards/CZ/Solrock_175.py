# Gallery print swsh12pt5gg/GG15; artwork is downloaded by the installer.
from spirit.game.scripts.cards.PGO.Solrock_39 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=175,
    rarity=Rarities.ChrRareHolo,
    guid='a03c0666-fc7d-5885-989a-69717aee4594',
    set_code='CZ',
    key='CZ',
    regulation_mark='F',
)

card.extra_attributes["200790"] = {"type": "string", "value": "GG15"}
