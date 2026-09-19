from spirit.game.scripts.cards.SWSH1.MorpekoV_79 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=56,
    rarity=Rarities.RarePromo,
    guid='b59e2418-12fc-59e1-bf33-775790c8f53e',
    set_code='Promo_SWSH',
    key='Promo_SWSH',
    regulation_mark='D',
)

card.extra_attributes['200790'] = {'type': 'string', 'value': 'SWSH056'}
