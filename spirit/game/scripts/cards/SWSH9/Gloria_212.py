# Gallery print swsh9tg/TG26; artwork is downloaded by the installer.
from spirit.game.scripts.cards.SWSH9.Gloria_141 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=212,
    rarity=Rarities.RareUltra,
    guid='8d249eef-52d2-52bd-8f96-892f3f2bba08',
    set_code='SWSH9',
    key='SWSH9',
    regulation_mark='E',
)

card.extra_attributes["200790"] = {"type": "string", "value": "TG26"}
