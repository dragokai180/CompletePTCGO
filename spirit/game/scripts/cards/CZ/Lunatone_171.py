# Gallery print swsh12pt5gg/GG11; artwork is downloaded by the installer.
from spirit.game.scripts.cards.PGO.Lunatone_34 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=171,
    rarity=Rarities.ChrRareHolo,
    guid='5e92f2de-5c9c-52e4-a469-e99a83de3f49',
    set_code='CZ',
    key='CZ',
    regulation_mark='F',
)

card.extra_attributes["200790"] = {"type": "string", "value": "GG11"}
