from spirit.game.scripts.cards.SV2.Pyroar_32 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=200,
    rarity=Rarities.ChrRareHolo,
    guid='65c93555-0c31-553a-bdfe-1e021c794113',
    set_code='SV2',
    key='SV2',
    regulation_mark='G',
)
