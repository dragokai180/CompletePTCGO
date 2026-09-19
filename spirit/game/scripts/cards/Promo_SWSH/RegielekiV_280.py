from spirit.game.scripts.cards.SWSH12.RegielekiV_57 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=280,
    rarity=Rarities.RarePromo,
    guid='80a9d211-a085-5acc-9305-244ec945ffb7',
    set_code='Promo_SWSH',
    key='Promo_SWSH',
    regulation_mark='F',
)

card.extra_attributes['200790'] = {'type': 'string', 'value': 'SWSH280'}
