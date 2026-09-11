from spirit.game.scripts.cards.Promo_SM.LunalaGX_103 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=250,
    rarity=Rarities.RarePromo,
    guid='f246fe26-83f3-5cb3-b632-fd7942d17a69',
    set_code='Promo_SM',
    key='Promo_SM',
    regulation_mark=None,
)
