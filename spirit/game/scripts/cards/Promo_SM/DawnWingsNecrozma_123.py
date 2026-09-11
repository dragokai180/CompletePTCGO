from spirit.game.scripts.cards.Promo_SM.DawnWingsNecrozma_106 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=123,
    rarity=Rarities.RarePromo,
    guid='0666f414-32cd-5e9a-a1ff-ef7dd9de7a7f',
    set_code='Promo_SM',
    key='Promo_SM',
    regulation_mark=None,
)
