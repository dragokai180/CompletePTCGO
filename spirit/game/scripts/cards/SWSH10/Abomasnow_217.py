# Gallery print swsh10tg/TG01; artwork is downloaded by the installer.
from spirit.game.scripts.cards.SWSH6.Abomasnow_10 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=217,
    rarity=Rarities.ChrRareHolo,
    guid='a03fd19a-0e2d-5264-bac7-6b65fcc8c577',
    set_code='SWSH10',
    key='SWSH10',
    regulation_mark='E',
)

card.extra_attributes["200790"] = {"type": "string", "value": "TG01"}
