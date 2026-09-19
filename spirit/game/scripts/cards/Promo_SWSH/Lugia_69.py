from spirit.game.scripts.cards.SWSH4.Lugia_132 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=69,
    rarity=Rarities.RarePromo,
    guid='fc228af2-912c-5df7-9d49-ca89e599eba8',
    set_code='Promo_SWSH',
    key='Promo_SWSH',
    regulation_mark='D',
)

card.extra_attributes['200790'] = {'type': 'string', 'value': 'SWSH069'}
