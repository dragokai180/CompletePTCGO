# Gallery print swsh12tg/TG05; artwork is downloaded by the installer.
from spirit.game.scripts.cards.SWSH12.Gardevoir_69 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=220,
    rarity=Rarities.ChrRareHolo,
    guid='00186787-1b98-5c17-8692-3a41744d2d0c',
    set_code='SWSH12',
    key='SWSH12',
    regulation_mark='F',
)

card.extra_attributes["200790"] = {"type": "string", "value": "TG05"}
