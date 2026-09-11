from spirit.game.scripts.cards.SV2.Saguaro_187 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=255,
    rarity=Rarities.RareUltra,
    guid='1d1c0eef-973a-5e37-a10f-d984b70e7346',
    set_code='SV2',
    key='SV2',
    regulation_mark='G',
)
