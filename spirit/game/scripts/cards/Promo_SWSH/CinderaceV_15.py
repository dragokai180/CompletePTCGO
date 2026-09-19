from spirit.game.scripts.cards.SWSH2.CinderaceV_35 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=15,
    rarity=Rarities.RarePromo,
    guid='7282d67c-f9f0-56da-a0b9-4dc30bc6e38d',
    set_code='Promo_SWSH',
    key='Promo_SWSH',
    regulation_mark='D',
)

card.extra_attributes['200790'] = {'type': 'string', 'value': 'SWSH015'}
