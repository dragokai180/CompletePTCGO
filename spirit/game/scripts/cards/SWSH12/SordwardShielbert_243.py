# Gallery print swsh12tg/TG28; artwork is downloaded by the installer.
from spirit.game.scripts.cards.SWSH5.SordwardShielbert_135 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=243,
    rarity=Rarities.RareUltra,
    guid='30973f6e-87d4-5bf4-8cc9-a10586e74b6e',
    set_code='SWSH12',
    key='SWSH12',
    regulation_mark='D',
)

card.extra_attributes["200790"] = {"type": "string", "value": "TG28"}
