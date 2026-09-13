# Gallery print swsh10tg/TG09; artwork is downloaded by the installer.
from spirit.game.scripts.cards.SWSH10.Mightyena_96 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=225,
    rarity=Rarities.ChrRareHolo,
    guid='2be47b28-eb22-53b6-b109-9dc04f7abe9c',
    set_code='SWSH10',
    key='SWSH10',
    regulation_mark='F',
)

card.extra_attributes["200790"] = {"type": "string", "value": "TG09"}
