# Gallery print swsh10tg/TG21; artwork is downloaded by the installer.
from spirit.game.scripts.cards.SWSH1.ZacianV_138 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=237,
    rarity=Rarities.RareHoloV,
    guid='3efcccdb-d897-56e4-8fd0-ee10b62e963a',
    set_code='SWSH10',
    key='SWSH10',
    regulation_mark='D',
)

card.extra_attributes["200790"] = {"type": "string", "value": "TG21"}
