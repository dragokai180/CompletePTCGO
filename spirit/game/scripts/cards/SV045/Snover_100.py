from spirit.game.scripts.cards.SV2.Snover_10 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=100,
    rarity=Rarities.Rare,
    guid='93298987-ca8c-517d-82fe-a11b28e02969',
    set_code='SV045',
    key='SV045',
    regulation_mark='G',
)
