from spirit.game.scripts.cards.SV07.Venusaurex_1 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=3,
    rarity=Rarities.RareHoloEX,
    guid='85545e1a-1e6d-52cd-a531-03e86ca4ba31',
    set_code='SV035',
    key='SV035',
    regulation_mark='G',
)
