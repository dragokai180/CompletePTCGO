from spirit.game.scripts.cards.SVP.Pikachu_190 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=225,
    rarity=Rarities.RarePromo,
    guid="fc97b181-5ddf-518d-ba4f-ef38cff5f0e3",
    set_code="SVP",
    key="SVP",
    regulation_mark="I",
)
