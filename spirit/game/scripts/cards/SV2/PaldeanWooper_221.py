from spirit.game.scripts.cards.SV2.PaldeanWooper_128 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=221,
    rarity=Rarities.ChrRareHolo,
    guid='5873d05a-f447-586b-96f1-441c41c45860',
    set_code='SV2',
    key='SV2',
    regulation_mark='G',
)
