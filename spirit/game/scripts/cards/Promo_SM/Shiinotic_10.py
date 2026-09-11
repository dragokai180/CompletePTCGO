from spirit.game.scripts.cards.SM1.Shiinotic_17 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=10,
    rarity=Rarities.RarePromo,
    guid='4a9896c8-761c-53bf-b93a-a150603339c0',
    set_code='Promo_SM',
    key='Promo_SM',
    regulation_mark=None,
)
