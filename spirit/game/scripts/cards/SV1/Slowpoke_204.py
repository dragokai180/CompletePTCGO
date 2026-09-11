from spirit.game.scripts.cards.SV1.Slowpoke_42 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=204,
    rarity=Rarities.ChrRareHolo,
    guid='bcddd829-4bb6-5468-9b4f-795c1abd7c18',
    set_code='SV1',
    key='SV1',
    regulation_mark='G',
)
