from spirit.game.scripts.cards.ME2.Gastly_54 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=123,
    rarity=Rarities.Common,
    guid="6086f296-5845-5feb-99c3-a2921e3c7e4d",
    set_code="ME2PT5",
    key="ME2PT5",
    regulation_mark="I",
)
