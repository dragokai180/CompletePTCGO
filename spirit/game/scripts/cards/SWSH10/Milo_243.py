# Gallery print swsh10tg/TG27; artwork is downloaded by the installer.
from spirit.game.scripts.cards.SWSH2.Milo_161 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=243,
    rarity=Rarities.RareUltra,
    guid='a869f528-5d62-5126-bc56-7c04024cf374',
    set_code='SWSH10',
    key='SWSH10',
    regulation_mark='D',
)

card.extra_attributes["200790"] = {"type": "string", "value": "TG27"}
