from spirit.game.scripts.cards.SV1.Penny_183 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=252,
    rarity=Rarities.RareSecret,
    guid='04f2cf86-4722-5215-b824-05c99e2b278b',
    set_code='SV1',
    key='SV1',
    regulation_mark='G',
)
