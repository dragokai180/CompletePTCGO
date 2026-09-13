# Gallery print swsh9tg/TG24; artwork is downloaded by the installer.
from spirit.game.scripts.cards.SWSH9.AcerolasPremonition_129 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=210,
    rarity=Rarities.RareUltra,
    guid='cf3faa0a-b061-5306-b231-e29e6acc3326',
    set_code='SWSH9',
    key='SWSH9',
    regulation_mark='E',
)

card.extra_attributes["200790"] = {"type": "string", "value": "TG24"}
