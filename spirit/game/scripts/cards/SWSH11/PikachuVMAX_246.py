# Gallery print swsh11tg/TG29; artwork is downloaded by the installer.
from spirit.game.scripts.cards.SWSH4.PikachuVMAX_44 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=246,
    rarity=Rarities.RareSecret,
    guid='24644e2f-192b-5efb-a239-51f288408879',
    set_code='SWSH11',
    key='SWSH11',
    regulation_mark='D',
)

card.extra_attributes["200790"] = {"type": "string", "value": "TG29"}
