# Gallery print swsh9tg/TG30; artwork is downloaded by the installer.
from spirit.game.scripts.cards.SWSH5.RapidStrikeUrshifuVMAX_88 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=216,
    rarity=Rarities.RareSecret,
    guid='843aa361-4e24-5638-a6ab-e6ab25895c95',
    set_code='SWSH9',
    key='SWSH9',
    regulation_mark='E',
)

card.extra_attributes["200790"] = {"type": "string", "value": "TG30"}
