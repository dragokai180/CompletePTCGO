# Gallery print swsh12pt5gg/GG63; artwork is downloaded by the installer.
from spirit.game.scripts.cards.SWSH10.Irida_147 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=223,
    rarity=Rarities.RareUltra,
    guid='3b8d8c88-39f3-568b-b6de-0bda124ab7b4',
    set_code='CZ',
    key='CZ',
    regulation_mark='F',
)

card.extra_attributes["200790"] = {"type": "string", "value": "GG63"}
