# Gallery print swsh12pt5gg/GG51; artwork is downloaded by the installer.
from spirit.game.scripts.cards.SWSH10.HisuianSamurottV_101 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=211,
    rarity=Rarities.RareHoloV,
    guid='d96d9554-e503-54c6-9790-369e91621fb1',
    set_code='CZ',
    key='CZ',
    regulation_mark='F',
)

card.extra_attributes["200790"] = {"type": "string", "value": "GG51"}
