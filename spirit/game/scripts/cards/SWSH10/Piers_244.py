# Gallery print swsh10tg/TG28; artwork is downloaded by the installer.
from spirit.game.scripts.cards.SWSH3.Piers_165 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=244,
    rarity=Rarities.RareUltra,
    guid='cd3bf0a1-ffc2-5d93-96d0-89640af97a00',
    set_code='SWSH10',
    key='SWSH10',
    regulation_mark='D',
)

card.extra_attributes["200790"] = {"type": "string", "value": "TG28"}
