from spirit.game.scripts.cards.ME3.Salazzleex_16 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=101,
    rarity=Rarities.RareUltra,
    guid="f105e3b6-ead9-5470-91a7-ce573690c2f8",
    set_code="ME3",
    key="ME3",
    regulation_mark="J",
)
