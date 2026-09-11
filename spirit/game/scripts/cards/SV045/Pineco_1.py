from spirit.game.scripts.cards.SV2.Pineco_4 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=1,
    rarity=Rarities.Common,
    guid='4c311c21-36cc-5f06-9e71-8d96049ab28c',
    set_code='SV045',
    key='SV045',
    regulation_mark='G',
)
