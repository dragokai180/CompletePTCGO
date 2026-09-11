from spirit.game.scripts.cards.SV035.Mewtwo_150 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=52,
    rarity=Rarities.RarePromo,
    guid='3366f9b2-de79-5329-b062-8879a828b413',
    set_code='SVP',
    key='SVP',
    regulation_mark='G',
)
