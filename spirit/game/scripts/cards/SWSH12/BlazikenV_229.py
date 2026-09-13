# Gallery print swsh12tg/TG14; artwork is downloaded by the installer.
from spirit.game.scripts.cards.SWSH6.BlazikenV_20 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=229,
    rarity=Rarities.RareHoloV,
    guid='ce16a3a5-223c-553e-84f6-1b181f1f650a',
    set_code='SWSH12',
    key='SWSH12',
    regulation_mark='E',
)

card.extra_attributes["200790"] = {"type": "string", "value": "TG14"}
