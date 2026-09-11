from spirit.game.scripts.cards.SV1.Pawmot_76 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=6,
    rarity=Rarities.RarePromo,
    guid='28535ab0-1e5d-53b9-8b4f-4297c9cdc438',
    set_code='SVP',
    key='SVP',
    regulation_mark='G',
)
