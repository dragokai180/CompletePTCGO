from spirit.game.scripts.cards.ME2.Rotomex_29 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=111,
    rarity=Rarities.RareUltra,
    guid="0c0005bf-5a5b-5eee-98e3-41b1ccd00256",
    set_code="ME2",
    key="ME2",
    regulation_mark="I",
)
