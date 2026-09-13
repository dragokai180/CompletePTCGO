# Gallery print swsh11tg/TG03; artwork is downloaded by the installer.
from spirit.game.scripts.cards.SWSH4.Charizard_25 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=220,
    rarity=Rarities.ChrRareHolo,
    guid='5ba844d8-f7d2-5aef-b985-18b254438c19',
    set_code='SWSH11',
    key='SWSH11',
    regulation_mark='D',
)

card.extra_attributes["200790"] = {"type": "string", "value": "TG03"}
