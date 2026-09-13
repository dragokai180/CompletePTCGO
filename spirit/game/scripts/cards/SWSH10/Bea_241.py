# Gallery print swsh10tg/TG25; artwork is downloaded by the installer.
from spirit.game.scripts.cards.SWSH4.Bea_147 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=241,
    rarity=Rarities.RareUltra,
    guid='5708e4c7-0a14-533b-9c7c-e07541852ac2',
    set_code='SWSH10',
    key='SWSH10',
    regulation_mark='D',
)

card.extra_attributes["200790"] = {"type": "string", "value": "TG25"}
