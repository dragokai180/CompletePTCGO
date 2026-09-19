from spirit.game.scripts.cards.SWSH12.Sunflora_6 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=269,
    rarity=Rarities.RarePromo,
    guid='2a8bde02-e404-5593-9f5c-09a1ea02f396',
    set_code='Promo_SWSH',
    key='Promo_SWSH',
    regulation_mark='F',
)

card.extra_attributes['200790'] = {'type': 'string', 'value': 'SWSH269'}
