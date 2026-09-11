from spirit.game.scripts.cards.SV4.Horsea_30 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=137,
    rarity=Rarities.RarePromo,
    guid='fe574776-41eb-5325-a086-4520f84dcef1',
    set_code='SVP',
    key='SVP',
    regulation_mark='G',
)
