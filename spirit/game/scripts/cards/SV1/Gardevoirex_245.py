from spirit.game.scripts.cards.SV1.Gardevoirex_86 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=245,
    rarity=Rarities.RareSecret,
    guid='4fe470fb-22cb-5df9-9ad8-c583fae701f1',
    set_code='SV1',
    key='SV1',
    regulation_mark='G',
)
