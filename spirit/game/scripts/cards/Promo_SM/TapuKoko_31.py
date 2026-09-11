from spirit.game.scripts.cards.Promo_SM.TapuKoko_30 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=31,
    rarity=Rarities.RarePromo,
    guid='cfcc17dd-a262-566a-8b2e-620769c3c0dc',
    set_code='Promo_SM',
    key='Promo_SM',
    regulation_mark=None,
)
