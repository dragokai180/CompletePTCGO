# Gallery print swsh10tg/TG12; artwork is downloaded by the installer.
from spirit.game.scripts.cards.SWSH10.Hoothoot_120 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=228,
    rarity=Rarities.ChrRareHolo,
    guid='ddfc7ddf-f9a8-54d5-bb19-b53c7c865f45',
    set_code='SWSH10',
    key='SWSH10',
    regulation_mark='F',
)

card.extra_attributes["200790"] = {"type": "string", "value": "TG12"}
