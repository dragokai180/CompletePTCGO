# Gallery print swsh10tg/TG11; artwork is downloaded by the installer.
from spirit.game.scripts.cards.SWSH5.Bronzong_102 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=227,
    rarity=Rarities.ChrRareHolo,
    guid='1880a3ee-d641-5c18-b47b-d01fc6fb7518',
    set_code='SWSH10',
    key='SWSH10',
    regulation_mark='E',
)

card.extra_attributes["200790"] = {"type": "string", "value": "TG11"}
