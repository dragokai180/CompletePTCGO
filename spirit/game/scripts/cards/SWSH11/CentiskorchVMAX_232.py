# Gallery print swsh11tg/TG15; artwork is downloaded by the installer.
from spirit.game.scripts.cards.SWSH3.CentiskorchVMAX_34 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=232,
    rarity=Rarities.RareHoloVMAX,
    guid='9201466c-eb12-593d-86ae-54d780287f13',
    set_code='SWSH11',
    key='SWSH11',
    regulation_mark='D',
)

card.extra_attributes["200790"] = {"type": "string", "value": "TG15"}
