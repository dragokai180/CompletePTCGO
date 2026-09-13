# Gallery print swsh12tg/TG04; artwork is downloaded by the installer.
from spirit.game.scripts.cards.SWSH12.Jynx_62 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=219,
    rarity=Rarities.ChrRareHolo,
    guid='9ad5217f-1d0d-5e55-90f2-dfb2c33e7edc',
    set_code='SWSH12',
    key='SWSH12',
    regulation_mark='F',
)

card.extra_attributes["200790"] = {"type": "string", "value": "TG04"}
