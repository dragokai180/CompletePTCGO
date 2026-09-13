# Gallery print swsh12pt5gg/GG25; artwork is downloaded by the installer.
from spirit.game.scripts.cards.SWSH9.Bibarel_121 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=185,
    rarity=Rarities.ChrRareHolo,
    guid='711d51a1-08b7-5c33-8039-26b446517cfc',
    set_code='CZ',
    key='CZ',
    regulation_mark='F',
)

card.extra_attributes["200790"] = {"type": "string", "value": "GG25"}
