from spirit.game.scripts.cards.DM.FieryFlint_60 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=80,
    rarity=Rarities.Uncommon,
    guid='11a64d81-279d-50cb-b505-2c853702f65c',
    set_code='DM',
    key='DM',
    regulation_mark=None,
)
