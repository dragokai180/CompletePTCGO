from spirit.game.scripts.cards.SV1.Smoliv_21 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=23,
    rarity=Rarities.RarePromo,
    guid='755219e7-78af-5a3e-b8cd-3a386dd82034',
    set_code='SVP',
    key='SVP',
    regulation_mark='G',
)
