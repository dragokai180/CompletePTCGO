# Gallery print swsh11tg/TG24; artwork is downloaded by the installer.
from spirit.game.scripts.cards.SWSH2.BosssOrders_154 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=241,
    rarity=Rarities.RareUltra,
    guid='1d6c28da-f578-59ff-bbba-c5dc21e51821',
    set_code='SWSH11',
    key='SWSH11',
    regulation_mark='D',
)

card.extra_attributes["200790"] = {"type": "string", "value": "TG24"}
