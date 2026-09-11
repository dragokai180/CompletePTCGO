from spirit.game.scripts.cards.SV1.Varoom_140 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=26,
    rarity=Rarities.RarePromo,
    guid='e759f252-3366-5aca-9822-b222ed6ca377',
    set_code='SVP',
    key='SVP',
    regulation_mark='G',
)
