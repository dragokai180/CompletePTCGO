# Gallery print swsh12tg/TG24; artwork is downloaded by the installer.
from spirit.game.scripts.cards.SWSH7.Gordie_149 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=239,
    rarity=Rarities.RareUltra,
    guid='b4e8aad0-f781-5e70-8d4f-1b62dfa4fb28',
    set_code='SWSH12',
    key='SWSH12',
    regulation_mark='E',
)

card.extra_attributes["200790"] = {"type": "string", "value": "TG24"}
