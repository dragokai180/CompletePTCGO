from spirit.game.scripts.cards.SWSH45.Eevee_52 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=118,
    rarity=Rarities.RarePromo,
    guid='b5779fbe-5b0f-52c5-a191-21f9d35137e1',
    set_code='Promo_SWSH',
    key='Promo_SWSH',
    regulation_mark='D',
)

card.extra_attributes['200790'] = {'type': 'string', 'value': 'SWSH118'}
