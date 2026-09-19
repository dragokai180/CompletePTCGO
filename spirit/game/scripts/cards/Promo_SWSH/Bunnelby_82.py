from spirit.game.scripts.cards.SWSH3.Bunnelby_150 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=82,
    rarity=Rarities.RarePromo,
    guid='2f1aa766-e106-5b86-bc7c-a7bfc49cc328',
    set_code='Promo_SWSH',
    key='Promo_SWSH',
    regulation_mark='D',
)

card.extra_attributes['200790'] = {'type': 'string', 'value': 'SWSH082'}
