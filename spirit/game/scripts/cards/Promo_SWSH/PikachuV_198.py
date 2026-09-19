from spirit.game.scripts.cards.SWSH9.PikachuV_157 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=198,
    rarity=Rarities.RarePromo,
    guid='8d35dedf-4b4d-5639-87ea-b1e561ac41d7',
    set_code='Promo_SWSH',
    key='Promo_SWSH',
    regulation_mark='F',
)

card.extra_attributes['200790'] = {'type': 'string', 'value': 'SWSH198'}
