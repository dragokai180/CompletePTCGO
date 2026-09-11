from spirit.game.scripts.cards.SV1.Dolliv_22 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=200,
    rarity=Rarities.ChrRareHolo,
    guid='8e4ef5d4-a0c8-587a-85a3-ded93d2a087c',
    set_code='SV1',
    key='SV1',
    regulation_mark='G',
)
