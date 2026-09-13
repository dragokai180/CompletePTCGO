# Gallery print swsh11tg/TG27; artwork is downloaded by the installer.
from spirit.game.scripts.cards.SWSH4.Nessa_157 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=244,
    rarity=Rarities.RareUltra,
    guid='79d7ccc0-c7b4-5658-b126-4d3ede23524a',
    set_code='SWSH11',
    key='SWSH11',
    regulation_mark='D',
)

card.extra_attributes["200790"] = {"type": "string", "value": "TG27"}
