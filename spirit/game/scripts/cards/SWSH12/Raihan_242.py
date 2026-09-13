# Gallery print swsh12tg/TG27; artwork is downloaded by the installer.
from spirit.game.scripts.cards.SWSH7.Raihan_152 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=242,
    rarity=Rarities.RareUltra,
    guid='225eeb4c-90c2-54cf-a1e8-59bc73d426ea',
    set_code='SWSH12',
    key='SWSH12',
    regulation_mark='E',
)

card.extra_attributes["200790"] = {"type": "string", "value": "TG27"}
