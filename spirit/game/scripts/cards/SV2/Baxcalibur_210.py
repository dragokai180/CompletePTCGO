from spirit.game.scripts.cards.SV2.Baxcalibur_60 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=210,
    rarity=Rarities.ChrRareHolo,
    guid='fa80a710-7739-5d31-846d-1ed1a043a297',
    set_code='SV2',
    key='SV2',
    regulation_mark='G',
)
