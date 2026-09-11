from spirit.game.scripts.cards.HGSS1.Donphan_40 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=42,
    rarity=Rarities.Uncommon,
    guid='c7a506c6-e20e-5b81-a7d5-9ea6b4ab200f',
    set_code='COL',
    key='COL',
    regulation_mark=None,
)
