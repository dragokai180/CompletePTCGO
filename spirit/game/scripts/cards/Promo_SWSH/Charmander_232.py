from spirit.game.scripts.cards.PGO.Charmander_8 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=232,
    rarity=Rarities.RarePromo,
    guid='e623596c-ede7-520f-936d-3f7e0a108e4a',
    set_code='Promo_SWSH',
    key='Promo_SWSH',
    regulation_mark='F',
)

card.extra_attributes['200790'] = {'type': 'string', 'value': 'SWSH232'}
