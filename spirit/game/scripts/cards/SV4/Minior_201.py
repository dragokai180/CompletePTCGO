from spirit.game.scripts.cards.SV4.Minior_99 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=201,
    rarity=Rarities.ChrRareHolo,
    guid='ef2d1d80-68d1-531b-9d21-2dd7b3dcbdb4',
    set_code='SV4',
    key='SV4',
    regulation_mark='G',
)
