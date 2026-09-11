from spirit.game.scripts.cards.SVE.BasicFireEnergy_2 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=10,
    rarity=Rarities.Common,
    guid='bee9ad80-46e6-5292-8881-42931f1d3fcb',
    set_code='SVE',
    key='SVE',
    regulation_mark=None,
)
