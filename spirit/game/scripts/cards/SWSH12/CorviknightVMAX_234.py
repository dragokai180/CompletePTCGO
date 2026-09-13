# Gallery print swsh12tg/TG19; artwork is downloaded by the installer.
from spirit.game.scripts.cards.SWSH5.CorviknightVMAX_110 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=234,
    rarity=Rarities.RareHoloVMAX,
    guid='39bbdcf8-5d31-50f2-80fd-cb3a24e09360',
    set_code='SWSH12',
    key='SWSH12',
    regulation_mark='E',
)

card.extra_attributes["200790"] = {"type": "string", "value": "TG19"}
