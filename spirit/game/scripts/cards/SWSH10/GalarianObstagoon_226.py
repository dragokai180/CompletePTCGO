# Gallery print swsh10tg/TG10; artwork is downloaded by the installer.
from spirit.game.scripts.cards.SWSH1.GalarianObstagoon_119 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=226,
    rarity=Rarities.ChrRareHolo,
    guid='4bbb755c-271a-59fa-92df-89a32b86a845',
    set_code='SWSH10',
    key='SWSH10',
    regulation_mark='D',
)

card.extra_attributes["200790"] = {"type": "string", "value": "TG10"}
