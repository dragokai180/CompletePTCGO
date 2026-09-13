# Gallery print swsh12pt5gg/GG08; artwork is downloaded by the installer.
from spirit.game.scripts.cards.SWSH9.Electivire_47 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=168,
    rarity=Rarities.ChrRareHolo,
    guid='3895e24d-4d0f-5661-9db9-e987a002ff14',
    set_code='CZ',
    key='CZ',
    regulation_mark='F',
)

card.extra_attributes["200790"] = {"type": "string", "value": "GG08"}
