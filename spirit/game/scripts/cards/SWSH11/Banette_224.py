# Gallery print swsh11tg/TG07; artwork is downloaded by the installer.
from spirit.game.scripts.cards.SWSH6.Banette_63 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=224,
    rarity=Rarities.ChrRareHolo,
    guid='9840d09c-8677-571c-a3ef-8f2ab96d99f9',
    set_code='SWSH11',
    key='SWSH11',
    regulation_mark='E',
)

card.extra_attributes["200790"] = {"type": "string", "value": "TG07"}
