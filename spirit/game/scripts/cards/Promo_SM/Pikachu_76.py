from spirit.game.scripts.cards.Promo_SM.Pikachu_4 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=76,
    rarity=Rarities.RarePromo,
    guid='48171dbd-406a-5884-b49f-60314b453305',
    set_code='Promo_SM',
    key='Promo_SM',
    regulation_mark=None,
)
