from spirit.game.scripts.cards.SWSH4.Charizard_25 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=66,
    rarity=Rarities.RarePromo,
    guid='fdc57bab-7184-54ed-9ca7-d9a2858c32c3',
    set_code='Promo_SWSH',
    key='Promo_SWSH',
    regulation_mark='D',
)

card.extra_attributes['200790'] = {'type': 'string', 'value': 'SWSH066'}
