# Gallery print swsh9tg/TG27; artwork is downloaded by the installer.
from spirit.game.scripts.cards.SWSH5.RapidStrikeStyleMustard_132 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=213,
    rarity=Rarities.RareUltra,
    guid='6ba583f6-b252-5393-b50c-d3028289c25a',
    set_code='SWSH9',
    key='SWSH9',
    regulation_mark='E',
)

card.extra_attributes["200790"] = {"type": "string", "value": "TG27"}
