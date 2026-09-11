from spirit.game.scripts.cards.SV2.Tinkaton_105 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=20,
    rarity=Rarities.RarePromo,
    guid='6a7ceb94-b042-5f68-8f17-84c531a659df',
    set_code='SVP',
    key='SVP',
    regulation_mark='G',
)
