from spirit.game.scripts.cards.SM1.Cosmog_64 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=42,
    rarity=Rarities.RarePromo,
    guid='a800ca3d-6856-5b29-aefc-4b6c7b07ed1d',
    set_code='Promo_SM',
    key='Promo_SM',
    regulation_mark=None,
)
