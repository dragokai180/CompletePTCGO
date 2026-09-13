# Gallery print swsh12tg/TG15; artwork is downloaded by the installer.
from spirit.game.scripts.cards.SWSH6.BlazikenVMAX_21 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=230,
    rarity=Rarities.RareHoloVMAX,
    guid='982e6c4a-5470-5189-b841-ffa57a54b10d',
    set_code='SWSH12',
    key='SWSH12',
    regulation_mark='E',
)

card.extra_attributes["200790"] = {"type": "string", "value": "TG15"}
