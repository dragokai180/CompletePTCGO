from spirit.game.scripts.cards.SV1.Greavard_104 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=42,
    rarity=Rarities.Common,
    guid='97b8cbd2-cd87-52c1-b960-1b6911f52ef9',
    set_code='SV045',
    key='SV045',
    regulation_mark='G',
)
