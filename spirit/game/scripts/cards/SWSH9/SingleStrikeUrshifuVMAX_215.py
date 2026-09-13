# Gallery print swsh9tg/TG29; artwork is downloaded by the installer.
from spirit.game.scripts.cards.SWSH5.SingleStrikeUrshifuVMAX_86 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=215,
    rarity=Rarities.RareSecret,
    guid='410fcf4e-9863-5686-8f32-fb11141567d6',
    set_code='SWSH9',
    key='SWSH9',
    regulation_mark='E',
)

card.extra_attributes["200790"] = {"type": "string", "value": "TG29"}
