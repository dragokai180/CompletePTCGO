# Gallery print swsh12tg/TG01; artwork is downloaded by the installer.
from spirit.game.scripts.cards.SWSH12.Braixen_26 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=216,
    rarity=Rarities.ChrRareHolo,
    guid='ed793162-1d5b-51ae-a31b-ab4088b1bdfb',
    set_code='SWSH12',
    key='SWSH12',
    regulation_mark='F',
)

card.extra_attributes["200790"] = {"type": "string", "value": "TG01"}
