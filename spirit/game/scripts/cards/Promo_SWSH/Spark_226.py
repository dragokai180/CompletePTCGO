from spirit.game.scripts.cards.PGO.Spark_70 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=226,
    rarity=Rarities.RarePromo,
    guid='17f73280-73d0-5f2e-8b68-5a598d7b4b43',
    set_code='Promo_SWSH',
    key='Promo_SWSH',
    regulation_mark='F',
)

card.extra_attributes['200790'] = {'type': 'string', 'value': 'SWSH226'}
