from spirit.game.scripts.cards.SWSH3.CrobatV_104 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=98,
    rarity=Rarities.RarePromo,
    guid='d267db85-b2ba-51a8-b105-bc89f3f9f769',
    set_code='Promo_SWSH',
    key='Promo_SWSH',
    regulation_mark='D',
)

card.extra_attributes['200790'] = {'type': 'string', 'value': 'SWSH098'}
