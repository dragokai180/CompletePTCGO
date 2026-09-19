from spirit.game.scripts.cards.SWSH12.Kirlia_68 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=271,
    rarity=Rarities.RarePromo,
    guid='8ddc47ef-f110-5a50-96f3-98c9ee1ae571',
    set_code='Promo_SWSH',
    key='Promo_SWSH',
    regulation_mark='F',
)

card.extra_attributes['200790'] = {'type': 'string', 'value': 'SWSH271'}
