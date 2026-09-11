from spirit.game.scripts.cards.DM.FieryFlint_60 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=76,
    rarity=Rarities.RareSecret,
    guid='a3ce3b39-962a-56d9-84b7-72d1dcfdea2a',
    set_code='DM',
    key='DM',
    regulation_mark=None,
)
