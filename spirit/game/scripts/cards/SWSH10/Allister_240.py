# Gallery print swsh10tg/TG24; artwork is downloaded by the installer.
from spirit.game.scripts.cards.SWSH4.Allister_146 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=240,
    rarity=Rarities.RareUltra,
    guid='e1f601ce-be5f-5dbd-be0b-3b568417c66d',
    set_code='SWSH10',
    key='SWSH10',
    regulation_mark='D',
)

card.extra_attributes["200790"] = {"type": "string", "value": "TG24"}
