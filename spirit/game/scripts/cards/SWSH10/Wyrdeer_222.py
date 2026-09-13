# Gallery print swsh10tg/TG06; artwork is downloaded by the installer.
from spirit.game.scripts.cards.SWSH10.Wyrdeer_69 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=222,
    rarity=Rarities.ChrRareHolo,
    guid='5d29375b-97af-5503-8ae7-476896616c8f',
    set_code='SWSH10',
    key='SWSH10',
    regulation_mark='F',
)

card.extra_attributes["200790"] = {"type": "string", "value": "TG06"}
