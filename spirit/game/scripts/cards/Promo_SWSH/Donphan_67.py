from spirit.game.scripts.cards.SWSH4.Donphan_87 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=67,
    rarity=Rarities.RarePromo,
    guid='afbc289e-b44b-58c0-9cef-3f66a09f17d7',
    set_code='Promo_SWSH',
    key='Promo_SWSH',
    regulation_mark='D',
)

card.extra_attributes['200790'] = {'type': 'string', 'value': 'SWSH067'}
