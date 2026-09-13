# Gallery print swsh12pt5gg/GG66; artwork is downloaded by the installer.
from spirit.game.scripts.cards.SWSH10.Roxanne_150 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=226,
    rarity=Rarities.RareUltra,
    guid='6162f1be-b610-584c-a796-493c16c5bbd9',
    set_code='CZ',
    key='CZ',
    regulation_mark='F',
)

card.extra_attributes["200790"] = {"type": "string", "value": "GG66"}
