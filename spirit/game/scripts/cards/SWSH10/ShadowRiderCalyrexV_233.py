# Gallery print swsh10tg/TG17; artwork is downloaded by the installer.
from spirit.game.scripts.cards.SWSH6.ShadowRiderCalyrexV_74 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=233,
    rarity=Rarities.RareHoloV,
    guid='75b04b31-a182-59a7-8171-7aa0fbc36154',
    set_code='SWSH10',
    key='SWSH10',
    regulation_mark='E',
)

card.extra_attributes["200790"] = {"type": "string", "value": "TG17"}
