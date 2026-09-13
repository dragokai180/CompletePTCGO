# Gallery print swsh11tg/TG05; artwork is downloaded by the installer.
from spirit.game.scripts.cards.SWSH11.Pikachu_52 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=222,
    rarity=Rarities.ChrRareHolo,
    guid='fa6d6077-5261-5d4a-ae03-7096759813c9',
    set_code='SWSH11',
    key='SWSH11',
    regulation_mark='F',
)

card.extra_attributes["200790"] = {"type": "string", "value": "TG05"}
