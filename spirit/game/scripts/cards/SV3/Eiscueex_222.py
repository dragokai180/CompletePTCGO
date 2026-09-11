from spirit.game.scripts.cards.SV3.Eiscueex_42 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=222,
    rarity=Rarities.RareSecret,
    guid='de1dd261-0780-5ea2-9d8c-13a0cecfd51a',
    set_code='SV3',
    key='SV3',
    regulation_mark='G',
)
