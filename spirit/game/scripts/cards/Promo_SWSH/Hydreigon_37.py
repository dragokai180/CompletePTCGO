from spirit.game.scripts.cards.SWSH3.Hydreigon_110 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=37,
    rarity=Rarities.RarePromo,
    guid='fdf53715-f6ef-5ce3-afdd-9991195cabf5',
    set_code='Promo_SWSH',
    key='Promo_SWSH',
    regulation_mark='D',
)

card.extra_attributes['200790'] = {'type': 'string', 'value': 'SWSH037'}
