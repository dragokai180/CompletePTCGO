from spirit.game.scripts.cards.SV07.Eevee_113 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=200,
    rarity=Rarities.RarePromo,
    guid="ee2d04b0-7983-51cf-b0b7-0c45e67f5dd3",
    set_code="SVP",
    key="SVP",
    regulation_mark="H",
)
