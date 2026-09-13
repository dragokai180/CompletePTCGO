# Gallery print swsh10tg/TG18; artwork is downloaded by the installer.
from spirit.game.scripts.cards.SWSH6.ShadowRiderCalyrexVMAX_75 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=234,
    rarity=Rarities.RareHoloVMAX,
    guid='afbaccf2-6a03-5a03-b8a7-984075eae122',
    set_code='SWSH10',
    key='SWSH10',
    regulation_mark='E',
)

card.extra_attributes["200790"] = {"type": "string", "value": "TG18"}
