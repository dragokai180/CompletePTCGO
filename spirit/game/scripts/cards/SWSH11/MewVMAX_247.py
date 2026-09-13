# Gallery print swsh11tg/TG30; artwork is downloaded by the installer.
from spirit.game.scripts.cards.SWSH8.MewVMAX_114 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=247,
    rarity=Rarities.RareSecret,
    guid='d91d9cd5-322b-5b6a-ad30-55d82d0191ec',
    set_code='SWSH11',
    key='SWSH11',
    regulation_mark='E',
)

card.extra_attributes["200790"] = {"type": "string", "value": "TG30"}
