# Gallery print swsh12pt5gg/GG29; artwork is downloaded by the installer.
from spirit.game.scripts.cards.CZ.Bidoof_111 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=189,
    rarity=Rarities.ChrRareHolo,
    guid='b10fa22b-ad95-5d6a-8e42-2e1ab351b4b7',
    set_code='CZ',
    key='CZ',
    regulation_mark='F',
)

card.extra_attributes["200790"] = {"type": "string", "value": "GG29"}
