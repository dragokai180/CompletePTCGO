from spirit.game.scripts.cards.SWSH1.Eldegoss_21 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=46,
    rarity=Rarities.RarePromo,
    guid='231de26d-0243-5573-823c-541f8d393942',
    set_code='Promo_SWSH',
    key='Promo_SWSH',
    regulation_mark='D',
)

card.extra_attributes['200790'] = {'type': 'string', 'value': 'SWSH046'}
