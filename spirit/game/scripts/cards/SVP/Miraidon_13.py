from spirit.game.scripts.cards.SV1.Miraidon_80 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=13,
    rarity=Rarities.RarePromo,
    guid='476053b8-569a-5528-a4a9-c81ae92d7457',
    set_code='SVP',
    key='SVP',
    regulation_mark='G',
)
