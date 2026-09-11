from spirit.game.scripts.cards.ME2.Nymble_9 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=96,
    rarity=Rarities.ChrRareHolo,
    guid="235b5aee-347f-5248-bcbc-0fa203d3a6c5",
    set_code="ME2",
    key="ME2",
    regulation_mark="I",
)
