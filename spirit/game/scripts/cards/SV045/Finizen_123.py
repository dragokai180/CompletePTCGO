from spirit.game.scripts.cards.SV3.Finizen_60 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=123,
    rarity=Rarities.Rare,
    guid='9b3b9c1a-5fa9-5bd1-a282-ee74773c1e19',
    set_code='SV045',
    key='SV045',
    regulation_mark='G',
)
