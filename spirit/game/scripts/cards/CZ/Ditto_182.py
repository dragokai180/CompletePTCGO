# Gallery print swsh12pt5gg/GG22; artwork is downloaded by the installer.
from spirit.game.scripts.cards.PGO.Ditto_53 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=182,
    rarity=Rarities.ChrRareHolo,
    guid='3171c2d7-401e-5876-b368-848e7f289993',
    set_code='CZ',
    key='CZ',
    regulation_mark='F',
)

card.extra_attributes["200790"] = {"type": "string", "value": "GG22"}
