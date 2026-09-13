# Gallery print swsh12tg/TG23; artwork is downloaded by the installer.
from spirit.game.scripts.cards.SWSH9.FriendsinGalar_140 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=238,
    rarity=Rarities.RareUltra,
    guid='473f8b5f-0d4d-5a75-a68e-09b72a4bcc7a',
    set_code='SWSH12',
    key='SWSH12',
    regulation_mark='E',
)

card.extra_attributes["200790"] = {"type": "string", "value": "TG23"}
