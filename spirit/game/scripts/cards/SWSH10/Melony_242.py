# Gallery print swsh10tg/TG26; artwork is downloaded by the installer.
from spirit.game.scripts.cards.SWSH6.Melony_146 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=242,
    rarity=Rarities.RareUltra,
    guid='a98bd149-c369-5404-9e43-3c6bf3a1ff31',
    set_code='SWSH10',
    key='SWSH10',
    regulation_mark='E',
)

card.extra_attributes["200790"] = {"type": "string", "value": "TG26"}
