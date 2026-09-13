# Gallery print swsh12pt5gg/GG30; artwork is downloaded by the installer.
from spirit.game.scripts.cards.SWSH11.Pikachu_52 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=190,
    rarity=Rarities.ChrRareHolo,
    guid='0099b9fe-01f2-583c-b6a8-fc1ed054490d',
    set_code='CZ',
    key='CZ',
    regulation_mark='F',
)

card.extra_attributes["200790"] = {"type": "string", "value": "GG30"}
