from spirit.game.scripts.cards.SWSH45.Eevee_52 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=42,
    rarity=Rarities.RarePromo,
    guid='89a6ef4a-7f9a-536d-9b31-4dcd3c3e6931',
    set_code='Promo_SWSH',
    key='Promo_SWSH',
    regulation_mark='D',
)

card.extra_attributes['200790'] = {'type': 'string', 'value': 'SWSH042'}
