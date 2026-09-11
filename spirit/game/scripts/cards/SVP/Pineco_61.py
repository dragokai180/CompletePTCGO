from spirit.game.scripts.cards.SV2.Pineco_4 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=61,
    rarity=Rarities.RarePromo,
    guid='47c925f4-ac42-5813-9857-e0cab2840747',
    set_code='SVP',
    key='SVP',
    regulation_mark='G',
)
