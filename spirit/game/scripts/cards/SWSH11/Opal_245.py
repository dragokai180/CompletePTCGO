# Gallery print swsh11tg/TG28; artwork is downloaded by the installer.
from spirit.game.scripts.cards.SWSH4.Opal_158 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=245,
    rarity=Rarities.RareUltra,
    guid='adc7037a-463b-53bc-b0d3-ad11d3d1d067',
    set_code='SWSH11',
    key='SWSH11',
    regulation_mark='D',
)

card.extra_attributes["200790"] = {"type": "string", "value": "TG28"}
