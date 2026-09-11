from spirit.game.scripts.cards.SV2.Baxcalibur_60 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=19,
    rarity=Rarities.RarePromo,
    guid='003a45df-31fc-59d8-8f0c-ab757a53432c',
    set_code='SVP',
    key='SVP',
    regulation_mark='G',
)
