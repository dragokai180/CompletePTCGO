# Gallery print swsh12tg/TG09; artwork is downloaded by the installer.
from spirit.game.scripts.cards.SWSH9.Druddigon_113 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=224,
    rarity=Rarities.ChrRareHolo,
    guid='31f1c07f-bd26-5711-9846-ce37e4b8ee0b',
    set_code='SWSH12',
    key='SWSH12',
    regulation_mark='E',
)

card.extra_attributes["200790"] = {"type": "string", "value": "TG09"}
