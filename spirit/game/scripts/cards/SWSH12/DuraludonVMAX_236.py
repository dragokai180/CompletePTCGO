# Gallery print swsh12tg/TG21; artwork is downloaded by the installer.
from spirit.game.scripts.cards.SWSH7.DuraludonVMAX_123 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=236,
    rarity=Rarities.RareHoloVMAX,
    guid='9f8cca40-6667-5ae2-a48f-eef80183f2ed',
    set_code='SWSH12',
    key='SWSH12',
    regulation_mark='E',
)

card.extra_attributes["200790"] = {"type": "string", "value": "TG21"}
