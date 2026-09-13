# Gallery print swsh12tg/TG11; artwork is downloaded by the installer.
from spirit.game.scripts.cards.SWSH12.Altaria_143 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=226,
    rarity=Rarities.ChrRareHolo,
    guid='f23c28cc-1219-5d97-aa8b-422a0cdbb64d',
    set_code='SWSH12',
    key='SWSH12',
    regulation_mark='F',
)

card.extra_attributes["200790"] = {"type": "string", "value": "TG11"}
