# Gallery print swsh12pt5gg/GG07; artwork is downloaded by the installer.
from spirit.game.scripts.cards.SWSH10.Keldeo_45 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=167,
    rarity=Rarities.ChrRareHolo,
    guid='860ff7db-23d4-56c3-b15a-83c0f4cecc63',
    set_code='CZ',
    key='CZ',
    regulation_mark='F',
)

card.extra_attributes["200790"] = {"type": "string", "value": "GG07"}
