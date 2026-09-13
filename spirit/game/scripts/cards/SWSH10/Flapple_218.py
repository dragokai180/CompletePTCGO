# Gallery print swsh10tg/TG02; artwork is downloaded by the installer.
from spirit.game.scripts.cards.SWSH2.Flapple_22 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=218,
    rarity=Rarities.ChrRareHolo,
    guid='708cf79e-e795-553b-8fc8-77ea7563a950',
    set_code='SWSH10',
    key='SWSH10',
    regulation_mark='D',
)

card.extra_attributes["200790"] = {"type": "string", "value": "TG02"}
