# Gallery print swsh12tg/TG25; artwork is downloaded by the installer.
from spirit.game.scripts.cards.SWSH8.Judge_235 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=240,
    rarity=Rarities.RareUltra,
    guid='4e39403d-1e34-5d44-bc87-7b554ad287e1',
    set_code='SWSH12',
    key='SWSH12',
    regulation_mark='E',
)

card.extra_attributes["200790"] = {"type": "string", "value": "TG25"}
