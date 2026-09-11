from spirit.game.scripts.cards.SM6.Rockruff_75 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=123,
    rarity=Rarities.Shining,
    guid='bae976d6-bad4-5e7e-b5b7-5e251ec640f8',
    set_code='HF',
    key='HF',
    regulation_mark=None,
)
