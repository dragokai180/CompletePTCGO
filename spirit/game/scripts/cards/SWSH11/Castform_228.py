# Gallery print swsh11tg/TG11; artwork is downloaded by the installer.
from spirit.game.scripts.cards.SWSH6.Castform_121 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=228,
    rarity=Rarities.ChrRareHolo,
    guid='79359854-86c3-58a6-b5f5-cf61a0df1db1',
    set_code='SWSH11',
    key='SWSH11',
    regulation_mark='E',
)

card.extra_attributes["200790"] = {"type": "string", "value": "TG11"}
