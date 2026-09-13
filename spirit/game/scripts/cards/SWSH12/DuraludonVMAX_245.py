# Gallery print swsh12tg/TG30; artwork is downloaded by the installer.
from spirit.game.scripts.cards.SWSH7.DuraludonVMAX_123 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=245,
    rarity=Rarities.RareSecret,
    guid='33baf0cd-3fa3-54e6-94df-5cde4f380a72',
    set_code='SWSH12',
    key='SWSH12',
    regulation_mark='E',
)

card.extra_attributes["200790"] = {"type": "string", "value": "TG30"}
