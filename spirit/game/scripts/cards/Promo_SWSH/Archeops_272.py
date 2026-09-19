from spirit.game.scripts.cards.SWSH12.Archeops_147 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=272,
    rarity=Rarities.RarePromo,
    guid='58b65c5f-7ff6-5c2c-aaf5-e19a759f3ee1',
    set_code='Promo_SWSH',
    key='Promo_SWSH',
    regulation_mark='F',
)

card.extra_attributes['200790'] = {'type': 'string', 'value': 'SWSH272'}
