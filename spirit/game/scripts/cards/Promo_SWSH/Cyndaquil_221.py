from spirit.game.scripts.cards.SWSH10.Cyndaquil_23 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=221,
    rarity=Rarities.RarePromo,
    guid='17f0cdd1-d6cd-50cd-b61c-b44cef9a91e5',
    set_code='Promo_SWSH',
    key='Promo_SWSH',
    regulation_mark='F',
)

card.extra_attributes['200790'] = {'type': 'string', 'value': 'SWSH221'}
