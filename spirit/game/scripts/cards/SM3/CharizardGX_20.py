from spirit.game.scripts.cards.Promo_SM.CharizardGX_60 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=20,
    rarity=Rarities.RareHoloGX,
    guid='6476f4c4-7334-5430-be25-d6726fd683d4',
    set_code='SM3',
    key='SM3',
    regulation_mark=None,
)
