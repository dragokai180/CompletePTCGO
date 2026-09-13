# Gallery print swsh10tg/TG05; artwork is downloaded by the installer.
from spirit.game.scripts.cards.SWSH6.Gardevoir_61 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=221,
    rarity=Rarities.ChrRareHolo,
    guid='00a20b89-ebe4-50d7-87b1-4708853aa077',
    set_code='SWSH10',
    key='SWSH10',
    regulation_mark='E',
)

card.extra_attributes["200790"] = {"type": "string", "value": "TG05"}
